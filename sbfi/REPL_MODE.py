from .utils import run_code
from sys import exit as xt

__all__ = [
    "BFREPLModeDoNotUseThisAsLibrary"
]

def BFREPLModeDoNotUseThisAsLibrary():
    try:
        while True:
            code = input("BF $ ")
            run_code(code)
    except Exception as e:
        print(f"\033[91m\033[1mError:\033[0m {e}")
        xt(0) 