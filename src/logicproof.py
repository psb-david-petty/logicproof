#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# logicproof.py
#
# TODO: --verbose only allows for two
#
"""
logicproof.py takes zero or more premises and compares them with a goal.

http://intrologic.stanford.edu/glossary/operator_precedence.html

The premises and the goal must be in postfix form with tokens separated by
spaces to ease parsing, for example:

    a & b | c & d => e                  # which would be parenthesized as:
    ((a & b) | (c & d)) => e            # is written in postfix form as:
    a b & c d & | e =>
"""

__author__ = "David C. Petty"
__copyright__ = "Copyright 2020, David C. Petty"
__license__ = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
__version__ = "0.0.2"
__maintainer__ = "David C. Petty"
__email__ = "david_petty@psbma.org"
__status__ = "Hack"

import argparse, os, re, sys


class Table:
    """Generate and print truth table for premises and goal."""
    _sep = '*'                              # table separator
    _emp = '+'                              # word emphasis
    _empty = ['T']                          # default empty premises
    _top = (0, lambda: 1)                   # true
    _nop = (1, lambda o: ~o & 1)            # not
    _aop = (2, lambda a, b: a & b)          # and
    _oop = (2, lambda a, b: a | b)          # or
    _iop = (2, lambda a, b: (~a | b) & 1)   # inference
    _bop = (2, lambda a, b: ~(a ^ b) & 1)   # biconditional
    # _ops is the dictionary of valid operation tuples.
    _ops = {'T': _top,                      # arity 0
            '~': _nop,                      # arity 1, arity 2
            '&': _aop, '|': _oop, '=>': _iop, '<=>': _bop, 'AND': _aop}

    def __init__(self, premises, goal, verbose=False):
        """Generate truth table for premises and goal."""
        self._premises = self._parse(premises)
        self._goals = self._parse(goal)
        assert len(self._goals) == 1, f"goal ({self._goals}) has > 1 item"
        self._verbose = verbose
        # Collect single-letter variable names from premises and goal, unless
        # premises is _empty.
        self._vars = set([t.lower() for exp in (
            self._premises if self._premises != self._empty else list())
            + self._goals for t in exp.split(' ')
            if t.lower() in 'abcdefghijklmnopqrstuvwxyz'])
        self._table = self._generate()

    """ ############### Table properties ############### """

    @property
    def premises(self):
        """Return self._premises list property."""
        return self._premises

    @property
    def goals(self):
        """Return self._goals list property."""
        return self._goals

    @property
    def table(self):
        """Return self._table multi-line string property."""
        return '\n'.join(self._table)

    @property
    def vars(self):
        """Return self._vars set property."""
        return self._vars

    @property
    def verbose(self):
        """Return self._verbose Boolean property."""
        return self._verbose

    """ ################ static methods ################ """

    @staticmethod
    def _parse(lines):
        """Return list of non-empty lines stripped of '#' comments."""
        return [
            (s[: s.find('#')] if s.find('#') >= 0 else s).strip()
            for s in lines.split('\n') if s
        ]

    @staticmethod
    def _values(n, var):
        """Return value dict for reversed sorted var list.
        For example, an n of 3 might yield {'a': 0, 'b': 1, 'c': '1'}"""
        assert 0 <= n < 2 ** len(var), f"{n} not on [0, 2 ** len({var}))"
        result = dict()
        for i, v in enumerate(reversed(sorted(var))):
            result[v] = (1 << i & n) >> i
        return result

    """ ############### instance methods ############### """

    def _evaluate_premises(self, n):
        """Return _evaluate of AND-conjoined premises for vars encoded w/ n."""
        return self._evaluate(
            ' '.join(self.premises + ['AND'] * (len(self.premises) - 1)),
            self._values(n, self.vars))

    def _evaluate_goal(self, n):
        """Return _evaluate of one-and-only goal for vars encoded w/ n"""
        return self._evaluate(self.goals[0], self._values(n, self.vars))

    def _markdown_encode(self, s):
        """Encode logic expressions for markdown table. In particular, the
        discunction symbol '|' is the same as the table cell delimiter."""
        an, aa, ao, ai, ab = '~', '&', '|', '=>', '<=>'
        un, ua, uo, ui, ub = '&not;', '&and;', '&or;', '&rArr;', '&hArr;'
        un, ua, uo, ui, ub = '\u00AC', '\u2227', '\u2228', '\u21D2', '\u21D4'
        ms, me = ' | ', '**'
        # ab must be replaced before ai, self._sep must be replaced after ao,
        # and self._emp must be replaced last.
        return s.replace(an, un)\
            .replace(aa, ua) \
            .replace(ao, uo) \
            .replace(ab, ub) \
            .replace(ai, ui) \
            .replace(self._sep, ms) \
            .replace(self._emp, me).strip()

    def _header(self):
        """Create two-line header for table."""
        dvb, nl, sep, wsq = '\u2016', '\n', self._sep, '\u25a1'
        vnames = f"{''.join(sorted(self.vars))}"
        pexp, pval = zip(*self._evaluate_premises(0))
        gexp, gval = zip(*self._evaluate_goal(0))
        header = self._markdown_encode(
            f"{sep}{vnames}{sep}{dvb}{sep}{sep.join(pexp)}{sep}" \
            f"{wsq}{sep}{sep.join(gexp)}{sep}")
        return header + '\n' \
            + f"{'| :---: ' * (len([c for c in header if c == '|']) - 1)}|"

    def _line(self, n):
        """Format table line."""
        dvb, sep, wsq = '\u2016', self._sep, '\u25a1'
        values, b = self._values(n, self.vars), lambda n: 'T' if n else 'F'
        pexp, pval = zip(*self._evaluate_premises(n))
        gexp, gval = zip(*self._evaluate_goal(n))
        number = \
            f"+{''.join(b(v) for v in values.values())[::-1]}+"
        line = self._markdown_encode(
            f"{sep}{number}{sep}{dvb}{sep}{sep.join(b(v) for v in pval)}{sep}" \
            f"{wsq}{sep}{sep.join(b(v) for v in gval)}{sep}")
        # TODO:
        if pval[-1]:
            return line.replace(wsq, '\u25a0')
        elif self.verbose:
            return line

    def _evaluate(self, exp, values):
        """Return (full_expression, evaluated_value, ) tuple that is result
        of evaluating exp in the context of values."""
        stack, calcs, sregex = list(), list(), re.compile(r'\s*')
        if exp in 'abcdefghijklmnopqrstuvwxyz':
            return [(exp, values[exp], )]
        for t in exp.split(' '):
            if t in 'abcdefghijklmnopqrstuvwxyz':
                # If t is a variable, push variable and value.
                stack.append((t, values[t],))
            elif t in self._ops:
                # If t is an op, evaluate push expression, push it and value.
                num, op = self._ops[t]  #
                pops = stack[-num: ]    #
                del stack[-num: ]       #
                exps, vals = zip(*pops) if pops else (list(), list(), )
                exp, val = ' '.join(list(exps) + [t]), op(*vals)
                stack.append((exp, val, ))
                calcs.append((exp, val,))
            else:
                print(f"unknown token: {t}")
        assert len(stack) == 1, f"unbalanced stack ({stack})"
        return calcs

    def _generate(self):
        # Evaluate all dicts.
        lines = [self._line(n) for n in range(2 ** len(self.vars))]
        return [self._header()] + [line for line in lines if line]


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
    """Collect command-line arguments, create Table, and print it."""
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
    parser.add_argument('PREMISE', nargs='*', help='zero or more premises')
    parser.add_argument('GOAL', help='goal to match to premise(s)')
    # Parse arguments.
    pa = parser.parse_args(args=argv[1: ])
    if not pa.PREMISE:
        pa.PREMISE = Table._empty
    if pa.ECHO:
        if pa.PREMISE:
            space, sq = '\n' + 11 * ' ', "'"
            print(f"PREMISES = " \
                  f"{f'{space}'.join([f'{sq}{p}{sq}' for p in pa.PREMISE])}")
        if pa.GOAL:
            print(f"    GOAL = '{pa.GOAL}'")
    # Create the truth table.
    table = Table('\n'.join(pa.PREMISE), pa.GOAL, pa.VERBOSE)
    # TODO: this simply prints the table
    print(table.table)


if __name__ == '__main__':
    is_idle, is_pycharm, is_jupyter = (
        'idlelib' in sys.modules,
        int(os.getenv('PYCHARM', 0)),
        '__file__' not in globals()
    )
    if any((is_idle, is_pycharm, is_jupyter,)):
        # Activity 4.3
        main(["logicproof.py", "-v", "-e",
              "s r &       # (S&R)",
              "a b s ~ & =># A=>(B&~S)",
              "a ~         # ~A", ])
        main(["logicproof.py",
              "a b &       # (a&b)",
              "p q a ~ & =># p=>(q&~a)",
              "p ~         # ~p", ])
        main(["logicproof.py", "-ev",
              "r s w & =>      # r => ( s & w )",
              "w r <=>         # w <=> r",
              "r ~ ~           # ~~r",
              "w q =>          # w => q",
              "s q & r <=>     # ( s & q ) <=> r", ])
        main(["logicproof.py", "-e",
              "r m & s w & =>         # (r&m)=>(s&w)",
              "r m & a & s w & b | => #  (r&m&a)=>(s&w|b)", ])
        main(["logicproof.py", "-e",
              "p q p => => # p=>(q=>p)", ])
        main(["logicproof.py", "-e",
              "p q |  # (p|q)",
              "p ~    # ~p",
              "q      # q"])
        main(["logicproof.py",
              "--help", ])
    else:
        main(sys.argv)
