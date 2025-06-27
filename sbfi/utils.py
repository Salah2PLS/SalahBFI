from .interpreter import BrainfInterpreter
import sys

__all__ = [
    "run_code",
    "exec_file"
]

bf = BrainfInterpreter()

def run_code(code: str, data_in: str = ""):
    bf.execute(code, data_in)

def exec_file(filename, data_in: str = ""):
    try:
        with open(filename, "r") as f:
            run_code(f.read)
    except FileNotFoundError:
        print("\033[91m\033[1mError:\033[0m file \"{file}\" does not exist.")
        sys.exit(1)

