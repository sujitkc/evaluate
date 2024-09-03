#!/usr/bin/python3

import sys
import subprocess
import evaluate as E

sys.path.append(".")
@E.evaluate
def eval_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  marks = 1
  from code import Q7
  from mycode import hello
  sub = lambda: Q7.hello("SKC")
  ref = lambda: hello.hello("SKC")
  return eval_matfun(fname, sub, ref)

eval_tests = testsuite(
  tests = [
    (eval_1, 1),
  ])

if __name__ == "__main__":
  print(eval_tests())
