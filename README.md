# logicproof

This script creates a truth-table proof and evaluates logical premises then compares them to an evaluated goal when the conjunction of all premises is `True`.

| Link | Description |
| -- | -- |
| [http://intrologic.stanford.edu/](http://intrologic.stanford.edu/) | Based on the *Stanford Introduction to Logic* course. |
| [http://logica.stanford.edu/logica/homepage/boole.php](http://logica.stanford.edu/logica/homepage/boole.php) | Similar to the [Logica](http://logica.stanford.edu/) Boole tool. |

The test proofs are based on activities from [Chapter 4](https://docs.google.com/presentation/d/e/2PACX-1vTg06S2eC-4g-GdnkG7_IzAX-ByUSugc_RlwGVb7FaEFgpVHH8L7rJkPGIZ_LqRmm0r2rqNMciuH3jX/pub).
## Usage

```
usage: logicproof.py [-?] [--version] [-e] [-v] [PREMISE [PREMISE ...]] GOAL

Collect one or more premises and a goal and display a truth table whose
entries are every combination of inputs where all premises are True.

positional arguments:
  PREMISE        zero or more premises (default: None)
  GOAL           goal to match to premise(s)

optional arguments:
  -?, --help     show this help message and exit
  --version      show program's version number and exit
  -e, --echo     echo premise(s) and goal (default: False)
  -v, --verbose  echo entire truth table (default: False)
```

## Example

```
$ /usr/bin/env python3 src/logicproof.py "-ev" \
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
| mpqrs | ‖ | q p ∧ | s q p ∧ ∨ | r s q p ∧ ∨ ∨ | m r ⇔ | q s ⇔ | q m ⇒ | q s ⇔ q m ⇒ AND | m r ⇔ q s ⇔ q m ⇒ AND AND | r s q p ∧ ∨ ∨ m r ⇔ q s ⇔ q m ⇒ AND AND AND | □ | m |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **00000** | ‖ | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | □ | 0 |
| **00001** | ‖ | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | □ | 0 |
| **00010** | ‖ | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | □ | 0 |
| **00011** | ‖ | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | □ | 0 |
| **00100** | ‖ | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | □ | 0 |
| **00101** | ‖ | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | □ | 0 |
| **00110** | ‖ | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | □ | 0 |
| **00111** | ‖ | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | □ | 0 |
| **01000** | ‖ | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | □ | 0 |
| **01001** | ‖ | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | □ | 0 |
| **01010** | ‖ | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | □ | 0 |
| **01011** | ‖ | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | □ | 0 |
| **01100** | ‖ | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | □ | 0 |
| **01101** | ‖ | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | □ | 0 |
| **01110** | ‖ | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | □ | 0 |
| **01111** | ‖ | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | □ | 0 |
| **10000** | ‖ | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | □ | 1 |
| **10001** | ‖ | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | □ | 1 |
| **10010** | ‖ | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | ■ | 1 |
| **10011** | ‖ | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | □ | 1 |
| **10100** | ‖ | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | □ | 1 |
| **10101** | ‖ | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | □ | 1 |
| **10110** | ‖ | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | □ | 1 |
| **10111** | ‖ | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | ■ | 1 |
| **11000** | ‖ | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | □ | 1 |
| **11001** | ‖ | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | □ | 1 |
| **11010** | ‖ | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | ■ | 1 |
| **11011** | ‖ | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | □ | 1 |
| **11100** | ‖ | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | □ | 1 |
| **11101** | ‖ | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | □ | 1 |
| **11110** | ‖ | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | □ | 1 |
| **11111** | ‖ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | ■ | 1 |
```
Which results in the following [markdown](https://github.github.com/gfm/):

| mpqrs | ‖ | q p ∧ | s q p ∧ ∨ | r s q p ∧ ∨ ∨ | m r ⇔ | q s ⇔ | q m ⇒ | q s ⇔ q m ⇒ AND | m r ⇔ q s ⇔ q m ⇒ AND AND | r s q p ∧ ∨ ∨ m r ⇔ q s ⇔ q m ⇒ AND AND AND | □ | m |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **00000** | ‖ | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | □ | 0 |
| **00001** | ‖ | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | □ | 0 |
| **00010** | ‖ | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | □ | 0 |
| **00011** | ‖ | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | □ | 0 |
| **00100** | ‖ | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | □ | 0 |
| **00101** | ‖ | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | □ | 0 |
| **00110** | ‖ | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | □ | 0 |
| **00111** | ‖ | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | □ | 0 |
| **01000** | ‖ | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | □ | 0 |
| **01001** | ‖ | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | □ | 0 |
| **01010** | ‖ | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | □ | 0 |
| **01011** | ‖ | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | □ | 0 |
| **01100** | ‖ | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | □ | 0 |
| **01101** | ‖ | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | □ | 0 |
| **01110** | ‖ | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | □ | 0 |
| **01111** | ‖ | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | □ | 0 |
| **10000** | ‖ | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | □ | 1 |
| **10001** | ‖ | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | □ | 1 |
| **10010** | ‖ | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | ■ | 1 |
| **10011** | ‖ | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | □ | 1 |
| **10100** | ‖ | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | □ | 1 |
| **10101** | ‖ | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | □ | 1 |
| **10110** | ‖ | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | □ | 1 |
| **10111** | ‖ | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | ■ | 1 |
| **11000** | ‖ | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | □ | 1 |
| **11001** | ‖ | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | □ | 1 |
| **11010** | ‖ | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | ■ | 1 |
| **11011** | ‖ | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | □ | 1 |
| **11100** | ‖ | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | □ | 1 |
| **11101** | ‖ | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | □ | 1 |
| **11110** | ‖ | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | □ | 1 |
| **11111** | ‖ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | ■ | 1 |

<hr>

[&#128279; permalink](https://psb-david-petty.github.io/logicproof) and [&#128297; repository](https://github.com/psb-david-petty/logicproof) for this page.
