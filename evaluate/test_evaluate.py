#!/usr/bin/python3

import evaluate as E

def t1():
  print(E.eval_program_stdin_stdout("t1", "1 2 3 4", "Q10"))

if __name__ == "__main__":
    t1()
