# logicproof

This script evaluates logical premises ...

## Usage

```
usage: logicproof.py [-?] [--version] [-e] [-v] PREMISE [PREMISE ...] GOAL

Collect one or more premises and a goal and display a truth table whose
entries are every combination of inputs where all premises are True.

positional arguments:
  PREMISE        one or more premises
  GOAL           goal to match to premise(s)

optional arguments:
  -?, --help     show this help message and exit
  --version      show program's version number and exit
  -e, --echo     echo premise(s) and goal (default: False)
  -v, --verbose  echo entire truth table (default: False)
```

## Example

```
$ /usr/bin/env python3 src/logicproof.py "-e" \
    "r s q p & | |  # (r|s|(q&p))" \
    "m r <=>        # m<=>r" \
    "q s <=>        # q<=>s" \
    "q m =>         # q=>m" \
    "m              # m"
```
```
PREMISES = 'r s q p & | |  # (r|s|(q&p))'
           'm r <=>        # m<=>r'
           'q s <=>        # q<=>s'
           'q m =>         # q=>m'
    GOAL = 'm              # m'
m:[1]p:[0]q:[0]r:[1]s:[0] ■ r s q p & | | m r <=> q s <=> q m => AND AND AND:[1] ⊫ m:[1] 
m:[1]p:[0]q:[1]r:[1]s:[1] ■ r s q p & | | m r <=> q s <=> q m => AND AND AND:[1] ⊫ m:[1] 
m:[1]p:[1]q:[0]r:[1]s:[0] ■ r s q p & | | m r <=> q s <=> q m => AND AND AND:[1] ⊫ m:[1] 
m:[1]p:[1]q:[1]r:[1]s:[1] ■ r s q p & | | m r <=> q s <=> q m => AND AND AND:[1] ⊫ m:[1] 
```
<hr>

[&#128279; permalink](https://psb-david-petty.github.io/logicproof) and [&#128297; repository](https://github.com/psb-david-petty/logicproof) for this page.
