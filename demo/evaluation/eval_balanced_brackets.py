#!/usr/bin/python3

import sys
import subprocess
import random
import evaluate as E

@E.evaluate
def eval_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  marks = 1
  from code import Q10
  from mycode import balanced_brackets
  s = "()"
  o = Q10.balanced_brackets(s)
  e = balanced_brackets.balanced_brackets(s)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

@E.evaluate
def eval_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q10
  from mycode import balanced_brackets
  s = "[]"
  o = Q10.balanced_brackets(s)
  e = balanced_brackets.balanced_brackets(s)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

@E.evaluate
def eval_3():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q10
  from mycode import balanced_brackets
  s = "{}"
  o = Q10.balanced_brackets(s)
  e = balanced_brackets.balanced_brackets(s)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

@E.evaluate
def eval_4():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  marks = 1
  from code import Q10
  from mycode import balanced_brackets
  s = ")("
  o = Q10.balanced_brackets(s)
  e = balanced_brackets.balanced_brackets(s)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

@E.evaluate
def eval_5():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q10
  from mycode import balanced_brackets
  s = "]["
  o = Q10.balanced_brackets(s)
  e = balanced_brackets.balanced_brackets(s)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

@E.evaluate
def eval_6():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q10
  from mycode import balanced_brackets
  s = "}{"
  o = Q10.balanced_brackets(s)
  e = balanced_brackets.balanced_brackets(s)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

@E.evaluate
def eval_7():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  marks = 1
  from code import Q10
  from mycode import balanced_brackets
  s = "((()())())"
  o = Q10.balanced_brackets(s)
  e = balanced_brackets.balanced_brackets(s)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

@E.evaluate
def eval_8():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q10
  from mycode import balanced_brackets
  s = "[[[][]][]]"
  o = Q10.balanced_brackets(s)
  e = balanced_brackets.balanced_brackets(s)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

@E.evaluate
def eval_9():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q10
  from mycode import balanced_brackets
  s = "{{{}{}}{}}"
  o = Q10.balanced_brackets(s)
  e = balanced_brackets.balanced_brackets(s)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

@E.evaluate
def eval_10():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  marks = 1
  from code import Q10
  from mycode import balanced_brackets
  s = "((()())"
  o = Q10.balanced_brackets(s)
  e = balanced_brackets.balanced_brackets(s)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

@E.evaluate
def eval_11():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q10
  from mycode import balanced_brackets
  s = "[[[][]]"
  o = Q10.balanced_brackets(s)
  e = balanced_brackets.balanced_brackets(s)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

@E.evaluate
def eval_12():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q10
  from mycode import balanced_brackets
  s = "{{{}{}}"
  o = Q10.balanced_brackets(s)
  e = balanced_brackets.balanced_brackets(s)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")



eval_tests = E.testsuite(
  tests = [
    (eval_1, 1),
    (eval_2, 1),
    (eval_3, 1),
    (eval_4, 1),
    (eval_5, 1),
    (eval_6, 1),
    (eval_7, 1),
    (eval_8, 1),
    (eval_9, 1),
    (eval_10, 1),
    (eval_11, 1),
    (eval_12, 1),
  ])

if __name__ == "__main__":
  print(eval_tests())
