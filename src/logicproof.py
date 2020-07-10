#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# logicproof.py
#
"""
logicproof.py takes one or more premises and compares them with the goal.
The premises and the goal must be in postfix form.
"""

__author__ = "David C. Petty"
__copyright__ = "Copyright 2020, David C. Petty"
__license__ = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
__version__ = "0.0.1"
__maintainer__ = "David C. Petty"
__email__ = "david_petty@psbma.org"
__status__ = "Hack"

import argparse, os, sys


class Table:
    sep = ' \u25a1 '

    def __init__(self, premises, goal, verbose=False):
        """"""
        self._premises = premises
        self._goal = goal
        self._verbose = verbose
        self.generate(self._premises, self._goal, self._verbose)

    def echo(self, exp, val, end=' '):
        """Print exp and val."""
        print(f"{exp}:[{val}]", end=end)

    def format_values(self, values):
        return ''.join([ f"{k}:[{values[k]}]" for k in sorted(values) ])

    def parse(self, lines):
        """Return list of lines stripped of comments."""
        return [
            (s[: s.find('#')] if s.find('#') >= 0 else s).strip()
            for s in lines.split('\n') if s
        ]

    def values(self, n, var):
        """Return value dict for reversed sorted var list."""
        assert 0 <= n < 2 ** len(var), f"{n} >= 2 ** len({var})"
        result = dict()
        for i, v in enumerate(reversed(sorted(var))):
            result[v] = (1 << i & n) >> i
        return result

    def evaluate(self, exp, values, verbose=True, echo_values=True):
        """Evaluate exp in the context of values."""
        if echo_values and verbose:
            print(self.format_values(values), end=self.sep)
        nop = (1, lambda o: ~o & 1)
        aop = (2, lambda a, b: a & b)
        oop = (2, lambda a, b: a | b)
        iop = (2, lambda a, b: (~a | b) & 1)
        bop = (2, lambda a, b: ~(a ^ b) & 1)
        ops = {'~': nop, '&': aop, '|': oop, '=>': iop, '<=>': bop, 'AND': aop}
        stack = list()
        for t in exp.split(' '):
            if t in 'abcdefghijklmnopqrstuvwxyz':
                stack.append((t, values[t],))
            elif t in ops:
                num, op = ops[t]        #
                pops = stack[-num: ]    #
                del stack[-num: ]       #
                exps, vals = list(pop[0] for pop in pops), list(pop[1] for pop in pops)
                stack.append((' '.join(list(exps) + [t]), op(*vals), ))
                if verbose:
                    self.echo(*stack[-1])
            else:
                print(f"unknown token: {t}")
        assert len(stack) == 1, f"unbalanced stack ({stack})"
        return stack.pop()

    def generate(self, premises, goal, verbose):
        p, g = self.parse(premises), self.parse(goal)
        assert len(g) == 1, f"goal ({g}) must only have one item"

        # Create token var list.
        var = set([t for exp in p + g for t in exp.split(' ')
                   if t in 'abcdefghijklmnopqrstuvwxyz'])

        # Evaluate all dicts.
        for n in range(2 ** len(var)):
            for exp in p:
                self.evaluate(exp, self.values(n, var), verbose)
                if verbose: print()
            exp, val = self.evaluate(' '.join(p + ['AND'] * (len(p) - 1)), self.values(n, var), verbose)
            # If val and gval, then the premises entail the conclusion.
            if val:
                if verbose: print()
                print(self.format_values(self.values(n, var)), end=' \u25a0 ')
                self.echo(exp, val); print('\u22ab', end=' ')
                gexp, gval = self.evaluate(g[0], self.values(n, var), False, False)
                self.echo(gexp, gval); print()
            elif verbose: print()


class Parser(argparse.ArgumentParser):
    """Create OptionParser to parse command-line options."""
    def __init__(self, **kargs):
        argparse.ArgumentParser.__init__(self, **kargs)
        # self.remove_argument("-h")
        self.add_argument("-?", "--help", action="help",
                          help="show this help message and exit")
        self.add_argument('--version', action='version',
                          version=f"%(prog)s {__version__}")

    def error(self, msg):
        sys.stderr.write("%s: error: %s\n\n" % (self.prog, msg, ))
        self.print_help()
        sys.exit(2)


def main(argv):
    """Collect command-line arguments and call  """
    description = """Collect one or more premises and a goal and display a 
    truth table whose entries are every combination of inputs where all 
    premises are True."""
    formatter = lambda prog: \
        argparse.ArgumentDefaultsHelpFormatter(prog, max_help_position=30)
    parser = Parser(description=description, add_help=False,
                    formatter_class=formatter)
    arguments = [
        # c1, c2, action, dest, default, help
        ('-e', '--echo', 'store_true', 'ECHO', False,
         'echo premise(s) and goal',),
        ('-v', '--verbose', 'store_true', 'VERBOSE', False,
         'echo entire truth table',),

    ]
    # Add optional arguments with values.
    for c1, c2, a, v, d, h in arguments:
        parser.add_argument(c1, c2, action=a, dest=v, default=d, help=h)
    # Add positional arguments. 'NAME' is both the string and the variable.
    parser.add_argument('PREMISE', nargs='+', help='one or more premises')
    parser.add_argument('GOAL', help='goal to match to premise(s)')
    # Parse arguments.
    pa = parser.parse_args(args=argv[1: ])
    if pa.ECHO:
        if pa.PREMISE:
            space, sq = '\n' + 11 * ' ', "'"
            print(f"PREMISES = " \
                  f"{f'{space}'.join([f'{sq}{p}{sq}' for p in pa.PREMISE])}")
        if pa.GOAL:
            print(f"    GOAL = '{pa.GOAL}'")
    # Create the truth table.
    # TODO: this simply prints the table
    table = Table('\n'.join(pa.PREMISE), pa.GOAL, pa.VERBOSE)


if __name__ == '__main__':
    is_idle, is_pycharm, is_jupyter = (
        'idlelib' in sys.modules,
        int(os.getenv('PYCHARM', 0)),
        '__file__' not in globals()
    )
    if any((is_idle, is_pycharm, is_jupyter,)):
        # Activity 4.3
        main(["logicproof.py", "-v",
              "s r &       # (S&R)",
              "a b s ~ & =># A=>(B&~S)",
              "a ~         # ~A", ])
        main(["logicproof.py",
              "a b &       # (a&b)",
              "p q a ~ & =># p=>(q&~a)",
              "p ~         # ~p", ])
        main(["logicproof.py", "-e",
              "r s w & =>      # r => ( s & w )",
              "w r <=>         # w <=> r",
              "r ~ ~           # ~~r",
              "w q =>          # w => q",
              "s q & r <=>     # ( s & q ) <=> r", ])
        main(["logicproof.py",
              "r m & s w & =>         # (r&m)=>(s&w)",
              "r m & a & s w & b | => #  (r&m&a)=>(s&w|b)", ])
        main(["logicproof.py",
              "--help", ])
    else:
        main(sys.argv)

# Activity 4.3
premises = """
s r & # (S&R)
a b s ~ & => # A=>(B&~S)
"""
goal = """
a ~ # ~A
"""
premises = """
a b & # (a&b)
p q a ~ & => # p=>(q&~a)
"""
goal = """
p ~ # ~p
"""
premises = """
r s w & =>      # r => ( s & w )
w r <=>         # w <=> r
r ~ ~           # ~~r
w q =>          # w => q
"""
goal = """
s q & r <=>     # ( s & q ) <=> r
"""
premises = """
r m & s w & => # (r&m)=>(s&w)
"""
goal = """
r m & a & s w & b | => #  (r&m&a)=>(s&w|b)
"""
