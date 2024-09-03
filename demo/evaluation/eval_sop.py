#!/usr/bin/python3

import sys
import subprocess
import random

sys.path.append("/home/sujit/IIITB/projects/evaluate/evaluate/")
import evaluate as E

t1 = [8, 2, 3]
t2 = [4, 9]
t3 = [1, 8, 5, 10]
t4 = [6, 6]
sop = [t1, t2, t3, t4]

@E.evaluate
def eval_product_of_list_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q3a as Sub
  from mycode import evaluate_SOP as Ref

  o = lambda: Sub.product_of_list(t3)
  e = lambda: Ref.product_of_list(t3)
  return E.eval_matfun(fname, o, e)

@E.evaluate
def eval_reduce_terms_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q3
  from mycode import evaluate_SOP as Ref

  o = lambda: Q3.reduce_terms(sop)
  e = lambda: Ref.reduce_terms(sop)
  return E.eval_matfun(fname, o, e)

@E.evaluate
def eval_reduce_terms_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  caller = "reduce_terms"
  callee = "product_of_list"
  return E.eval_f_calls_g(fname, "code/Q3.py", caller, callee)

@E.evaluate
def eval_sum_of_list_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q3
  from mycode import evaluate_SOP as Ref

  terms = Ref.reduce_terms(sop)

  o = lambda: Q3.sum_of_list(terms)
  e = lambda: Ref.sum_of_list(terms)
  return E.eval_matfun(fname, o, e)

@E.evaluate
def eval_evaluate_SOP_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q3
  from mycode import evaluate_SOP as Ref

  o = lambda: Q3.evaluate_SOP(sop)
  e = lambda: Ref.evaluate_SOP(sop)
  return E.eval_matfun(fname, o, e)

@E.evaluate
def eval_evaluate_SOP_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  caller = "evaluate_SOP"
  callee = "reduce_terms"
  return E.eval_f_calls_g(fname, "code/Q3.py", caller, callee)

@E.evaluate
def eval_evaluate_SOP_3():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  caller = "evaluate_SOP"
  callee = "sum_of_list"
  return E.eval_f_calls_g(fname, "code/Q3.py", caller, callee)

tests = [
  (eval_product_of_list_1, 1),
  (eval_reduce_terms_1, 1),
  (eval_reduce_terms_2, 2),
  (eval_sum_of_list_1, 1),
  (eval_evaluate_SOP_1, 1),
  (eval_evaluate_SOP_2, 2),
  (eval_evaluate_SOP_3, 2),
]

eval_tests = E.testsuite(
  tests = tests
)

if __name__ == "__main__":
  total = sum([m for (_, m) in tests])
  print("total marks = ", total)
  print(eval_tests())
