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
| **FFFFF** | ‖ | F | F | F | T | T | T | T | T | F | □ | F |
| **FFFFT** | ‖ | F | T | T | T | F | T | F | F | F | □ | F |
| **FFFTF** | ‖ | F | F | T | F | T | T | T | F | F | □ | F |
| **FFFTT** | ‖ | F | T | T | F | F | T | F | F | F | □ | F |
| **FFTFF** | ‖ | F | F | F | T | F | F | F | F | F | □ | F |
| **FFTFT** | ‖ | F | T | T | T | T | F | F | F | F | □ | F |
| **FFTTF** | ‖ | F | F | T | F | F | F | F | F | F | □ | F |
| **FFTTT** | ‖ | F | T | T | F | T | F | F | F | F | □ | F |
| **FTFFF** | ‖ | F | F | F | T | T | T | T | T | F | □ | F |
| **FTFFT** | ‖ | F | T | T | T | F | T | F | F | F | □ | F |
| **FTFTF** | ‖ | F | F | T | F | T | T | T | F | F | □ | F |
| **FTFTT** | ‖ | F | T | T | F | F | T | F | F | F | □ | F |
| **FTTFF** | ‖ | T | T | T | T | F | F | F | F | F | □ | F |
| **FTTFT** | ‖ | T | T | T | T | T | F | F | F | F | □ | F |
| **FTTTF** | ‖ | T | T | T | F | F | F | F | F | F | □ | F |
| **FTTTT** | ‖ | T | T | T | F | T | F | F | F | F | □ | F |
| **TFFFF** | ‖ | F | F | F | F | T | T | T | F | F | □ | T |
| **TFFFT** | ‖ | F | T | T | F | F | T | F | F | F | □ | T |
| **TFFTF** | ‖ | F | F | T | T | T | T | T | T | T | ■ | T |
| **TFFTT** | ‖ | F | T | T | T | F | T | F | F | F | □ | T |
| **TFTFF** | ‖ | F | F | F | F | F | T | F | F | F | □ | T |
| **TFTFT** | ‖ | F | T | T | F | T | T | T | F | F | □ | T |
| **TFTTF** | ‖ | F | F | T | T | F | T | F | F | F | □ | T |
| **TFTTT** | ‖ | F | T | T | T | T | T | T | T | T | ■ | T |
| **TTFFF** | ‖ | F | F | F | F | T | T | T | F | F | □ | T |
| **TTFFT** | ‖ | F | T | T | F | F | T | F | F | F | □ | T |
| **TTFTF** | ‖ | F | F | T | T | T | T | T | T | T | ■ | T |
| **TTFTT** | ‖ | F | T | T | T | F | T | F | F | F | □ | T |
| **TTTFF** | ‖ | T | T | T | F | F | T | F | F | F | □ | T |
| **TTTFT** | ‖ | T | T | T | F | T | T | T | F | F | □ | T |
| **TTTTF** | ‖ | T | T | T | T | F | T | F | F | F | □ | T |
| **TTTTT** | ‖ | T | T | T | T | T | T | T | T | T | ■ | T |
```
Which results in the following [markdown](https://github.github.com/gfm/):

| mpqrs | ‖ | q p ∧ | s q p ∧ ∨ | r s q p ∧ ∨ ∨ | m r ⇔ | q s ⇔ | q m ⇒ | q s ⇔ q m ⇒ AND | m r ⇔ q s ⇔ q m ⇒ AND AND | r s q p ∧ ∨ ∨ m r ⇔ q s ⇔ q m ⇒ AND AND AND | □ | m |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **FFFFF** | ‖ | F | F | F | T | T | T | T | T | F | □ | F |
| **FFFFT** | ‖ | F | T | T | T | F | T | F | F | F | □ | F |
| **FFFTF** | ‖ | F | F | T | F | T | T | T | F | F | □ | F |
| **FFFTT** | ‖ | F | T | T | F | F | T | F | F | F | □ | F |
| **FFTFF** | ‖ | F | F | F | T | F | F | F | F | F | □ | F |
| **FFTFT** | ‖ | F | T | T | T | T | F | F | F | F | □ | F |
| **FFTTF** | ‖ | F | F | T | F | F | F | F | F | F | □ | F |
| **FFTTT** | ‖ | F | T | T | F | T | F | F | F | F | □ | F |
| **FTFFF** | ‖ | F | F | F | T | T | T | T | T | F | □ | F |
| **FTFFT** | ‖ | F | T | T | T | F | T | F | F | F | □ | F |
| **FTFTF** | ‖ | F | F | T | F | T | T | T | F | F | □ | F |
| **FTFTT** | ‖ | F | T | T | F | F | T | F | F | F | □ | F |
| **FTTFF** | ‖ | T | T | T | T | F | F | F | F | F | □ | F |
| **FTTFT** | ‖ | T | T | T | T | T | F | F | F | F | □ | F |
| **FTTTF** | ‖ | T | T | T | F | F | F | F | F | F | □ | F |
| **FTTTT** | ‖ | T | T | T | F | T | F | F | F | F | □ | F |
| **TFFFF** | ‖ | F | F | F | F | T | T | T | F | F | □ | T |
| **TFFFT** | ‖ | F | T | T | F | F | T | F | F | F | □ | T |
| **TFFTF** | ‖ | F | F | T | T | T | T | T | T | T | ■ | T |
| **TFFTT** | ‖ | F | T | T | T | F | T | F | F | F | □ | T |
| **TFTFF** | ‖ | F | F | F | F | F | T | F | F | F | □ | T |
| **TFTFT** | ‖ | F | T | T | F | T | T | T | F | F | □ | T |
| **TFTTF** | ‖ | F | F | T | T | F | T | F | F | F | □ | T |
| **TFTTT** | ‖ | F | T | T | T | T | T | T | T | T | ■ | T |
| **TTFFF** | ‖ | F | F | F | F | T | T | T | F | F | □ | T |
| **TTFFT** | ‖ | F | T | T | F | F | T | F | F | F | □ | T |
| **TTFTF** | ‖ | F | F | T | T | T | T | T | T | T | ■ | T |
| **TTFTT** | ‖ | F | T | T | T | F | T | F | F | F | □ | T |
| **TTTFF** | ‖ | T | T | T | F | F | T | F | F | F | □ | T |
| **TTTFT** | ‖ | T | T | T | F | T | T | T | F | F | □ | T |
| **TTTTF** | ‖ | T | T | T | T | F | T | F | F | F | □ | T |
| **TTTTT** | ‖ | T | T | T | T | T | T | T | T | T | ■ | T |

<hr>

[&#128279; permalink](https://psb-david-petty.github.io/logicproof) and [&#128297; repository](https://github.com/psb-david-petty/logicproof) for this page.
