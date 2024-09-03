#!/usr/bin/python3

import sys
import subprocess
import random
import evaluate as E

@E.evaluate
def eval_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q11
  from mycode import mattrans
  m = [[12, 14],[16, 18],[20, 22]]
  sub = lambda: Q11.mattrans(m)
  ref = lambda: mattrans.mattrans(m)
  return eval_matfun(fname, sub, ref)

@E.evaluate
def eval_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q11
  from mycode import mattrans
  m = [[12, 14],[16, 18],[20, 22]]
  m = mattrans.mattrans(m)
  sub = lambda: Q11.mattrans(m)
  ref = lambda: mattrans.mattrans(m)
  return eval_matfun(fname, sub, ref)

eval_tests = testsuite(
  tests = [
    (eval_1, 1),
    (eval_2, 1),
  ])

if __name__ == "__main__":
  print(eval_tests())
