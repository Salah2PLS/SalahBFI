# SBFI - Salah's BrainF**k Interpreter

**SBFI** is a simple, lightweight, and not that fast, but fast interpreter for the Brainf**k programming language written in pure Python. It supports standard Brainf**k instructions, customizable I/O, and can be used both as a CLI tool and as a Python library.

---
***This page may contain errors or incorrect information. Please report any errors you may find.***
---
## Installation

You can clone the repository:

```bash
git clone https://github.com/SBFI-Project/SBFI-Project.git
cd SBFI-main

# for building
pip install build
python -m build # that will build the image automatically 
```

or, you can visit its repository and download `.whl` from available builds.

note: pypi images "***may***" be available soon.
---

## Quick Start

### As a Python Library

```python
from sbfi.utils import *

run_code("++++[>++++<-]>+.")
```

### Using the Interpreter Class

```python
from sbfi import BrainfInterpreter

code = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
interpreter = BrainfInterpreter()
interpreter.execute(code)

# this code outputs a status dump to "salahbf-dump.json"
interpreter.get_dump()
```

---

## Running `.bf` Files

You can run a Brainf**k file using the command line:

```bash
sbfi -r file.bf # add "-dmps/--dump-status" if you want to output interpreter status after Execution
```

---
## Supported Instructions

| Instruction | Description                      |
|-------------|----------------------------------|
| `>`         | Move pointer to the right        |
| `<`         | Move pointer to the left         |
| `+`         | Increment the cell at the pointer|
| `-`         | Decrement the cell at the pointer|
| `.`         | Output the character at pointer  |
| `,`         | Input a character to pointer     |
| `[`         | Jump forward if cell is 0        |
| `]`         | Jump backward if cell is not 0   |

---

## Project Structure

```
sbfi/
│── README.md
│── sbfi/
│   |── __init__.py
│   |── utils.py
│   └── interpreter.py
│── scripts/
│   └── sbfi    # comand-line tool
README.md
setup.py
```

---

## Features

- Fully compliant Brainf**k interpreter
- Clean and minimal API
- Customizable tape size
- Optional input/output redirection
- CLI support for running `.bf` files
- Easily embeddable in your Python projects

---

## License

This project is licensed under the MIT License.

---

## Author

Developed by **Salah Al-Refai**

---

## Contributions

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit a pull request.

