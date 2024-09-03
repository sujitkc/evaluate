#!/usr/bin/python3

import sys
import subprocess
import random

sys.path.append("/home/sujit/IIITB/projects/evaluate/evaluate/") #location of evaluate package.
import evaluate as E

@E.evaluate
def eval_increment():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q2
  from mycode import mathop

  n = random.randint(1, 100)
  o = lambda: Q2.increment(n)
  e = lambda: mathop.increment(n)
  return E.eval_matfun(fname, o, e)

@E.evaluate
def eval_decrement():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q2
  from mycode import mathop

  n = random.randint(1, 100)
  o = lambda: Q2.decrement(n)
  e = lambda: mathop.decrement(n)
  return E.eval_matfun(fname, o, e)

@E.evaluate
def eval_add_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q2
  from mycode import mathop

  x = random.randint(1, 100)
  y = random.randint(1, 100)
  o = lambda: Q2.add(x, y)
  e = lambda: mathop.add(x, y)
  return E.eval_matfun(fname, o, e)

@E.evaluate
def eval_add_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  caller = "add"
  callee = "increment"
  if(E.f_calls_g("code/Q2.py", caller, callee)):
    return(1, fname)
  else:
    return(0, fname + " : " + caller + " doesn't call " + callee + ".")
 
@E.evaluate
def eval_subtract_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q2
  from mycode import mathop

  x = random.randint(1, 100)
  y = random.randint(1, 100)
  o = lambda: Q2.subtract(x, y)
  e = lambda: mathop.subtract(x, y)
  return E.eval_matfun(fname, o, e)

@E.evaluate
def eval_subtract_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  caller = "subtract"
  callee = "decrement"
  if(E.f_calls_g("code/Q2.py", caller, callee)):
    return(1, fname)
  else:
    return(0, fname + " : " + caller + " doesn't call " + callee + ".")
 
@E.evaluate
def eval_multiply_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q2
  from mycode import mathop

  x = random.randint(1, 100)
  y = random.randint(1, 100)
  o = lambda: Q2.multiply(x, y)
  e = lambda: mathop.multiply(x, y)
  return E.eval_matfun(fname, o, e)

@E.evaluate
def eval_multiply_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  caller = "multiply"
  callee = "add"
  if(E.f_calls_g("code/Q2.py", caller, callee)):
    return(1, fname)
  else:
    return(0, fname + " : " + caller + " doesn't call " + callee + ".")

@E.evaluate
def eval_divide_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q2
  from mycode import mathop

  y = random.randint(1, 1000)
  x = random.randint(1, 100) * y
  o = lambda: Q2.divide(x, y)
  e = lambda: mathop.divide(x, y)
  return E.eval_matfun(fname, o, e)

@E.evaluate
def eval_divide_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  caller = "divide"
  callee = "subtract"
  if(E.f_calls_g("code/Q2.py", caller, callee)):
    return(1, fname)
  else:
    return(0, fname + " : " + caller + " doesn't call " + callee + ".")


@E.evaluate
def eval_exponent_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q2
  from mycode import mathop

  y = 23
  x = 3
  o = lambda: Q2.exponent(x, y)
  e = lambda: mathop.exponent(x, y)
  return E.eval_matfun(fname, o, e)

@E.evaluate
def eval_exponent_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  caller = "exponent"
  callee = "multiply"
  if(E.f_calls_g("code/Q2.py", caller, callee)):
    return(1, fname)
  else:
    return(0, fname + " : " + caller + " doesn't call " + callee + ".")


tests = [
  (eval_increment, 1),
  (eval_decrement, 1),
  (eval_add_1, 1),
  (eval_add_2, 2),
  (eval_subtract_1, 1),
  (eval_subtract_2, 2),
  (eval_multiply_1, 1),
  (eval_multiply_2, 2),
  (eval_divide_1, 1),
  (eval_divide_2, 2),
  (eval_exponent_1, 1),
  (eval_exponent_2, 2),
]
eval_tests = E.testsuite(
  tests = tests
)

if __name__ == "__main__":
  total = sum([m for (_, m) in tests])
  print("total marks = ", total)
  print(eval_tests())
