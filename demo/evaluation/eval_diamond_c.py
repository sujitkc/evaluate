#!/usr/bin/python3

import sys
import subprocess
import evaluate as E

@E.evaluate
def eval_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name
  return eval_named_proc_1(fname, driver = "diamond_c_driver.py")

eval_tests = testsuite(
  tests = [
    (eval_1, 1),
  ])

if __name__ == "__main__":
  print(eval_tests())
