#!/usr/bin/python3

import sys
import subprocess
import random

sys.path.append("/home/sujit/IIITB/projects/evaluate/evaluate/")
import evaluate as E

l1 = [12, 14]
l2 = [12, 14]
m1 = [l1,l2]
m2 = [l1,l2]

@E.evaluate
def eval_is_wellformed_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.is_wellformed(m1)
  ref = lambda: Ref.is_wellformed(m1)
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_is_wellformed_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.is_wellformed([])
  ref = lambda: Ref.is_wellformed([])
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_is_wellformed_3():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.is_wellformed([[]])
  ref = lambda: Ref.is_wellformed([[]])
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_is_wellformed_4():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.is_wellformed([[1, 2, 3], [1, 2]])
  ref = lambda: Ref.is_wellformed([[1, 2, 3], [1, 2]])
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_are_addable_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.are_addable(m1, m2)
  ref = lambda: Ref.are_addable(m1, m2)
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_are_addable_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.are_addable(m1, m2 + [[3, 4]])
  ref = lambda: Ref.are_addable(m1, m2 + [[3, 4]])
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_are_addable_3():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.are_addable(m1 + [[3, 4]], m2)
  ref = lambda: Ref.are_addable(m1 + [[3, 4]], m2)
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_are_addable_4():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.are_addable(m1 + [[3]], m2)
  ref = lambda: Ref.are_addable(m1 + [[3]], m2)
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_are_addable_5():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.are_addable(m1, m2 + [[3]])
  ref = lambda: Ref.are_addable(m1, m2 + [[3]])
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_are_addable_6():
  fname = __name__ + "." + sys._getframe().f_code.co_name
  return E.eval_f_calls_g(fname, "code/Q4.py", "are_addable", "is_wellformed") 

@E.evaluate
def eval_are_multipliable_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.are_multipliable(m1, m2)
  ref = lambda: Ref.are_multipliable(m1, m2)
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_are_multipliable_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.are_multipliable(m1 + [[3, 4]], m2)
  ref = lambda: Ref.are_multipliable(m1 + [[3, 4]], m2)
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_are_multipliable_3():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.are_multipliable(m1, m2 + [[3, 4]])
  ref = lambda: Ref.are_multipliable(m1, m2 + [[3, 4]])
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_are_multipliable_4():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.are_multipliable(m1 + [[3]], m2)
  ref = lambda: Ref.are_multipliable(m1 + [[3]], m2)
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_are_multipliable_5():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.are_multipliable([[1, 2]], [[34]])
  ref = lambda: Ref.are_multipliable([[1, 2]], [[34]])
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_are_multipliable_6():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.are_multipliable([[1]], [[34], [12]])
  ref = lambda: Ref.are_multipliable([[1]], [[34], [12]])
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_are_multipliable_7():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.are_multipliable(m1, m2 + [[34]])
  ref = lambda: Ref.are_multipliable(m1, m2 + [[34]])
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_are_multipliable_8():
  fname = __name__ + "." + sys._getframe().f_code.co_name
  return E.eval_f_calls_g(fname, "code/Q4.py", "are_multipliable", "is_wellformed") 

@E.evaluate
def eval_scalar_multiply_list_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.scalar_multiply_list(23, l2)
  ref = lambda: Ref.scalar_multiply_list(23, l2)
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_scalar_multiply_matrix_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.scalar_multiply_matrix(23, m2)
  ref = lambda: Ref.scalar_multiply_matrix(23, m2)
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_scalar_multiply_matrix_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  caller = "scalar_multiply_matrix"
  callee = "scalar_multiply_list"
  return E.eval_f_calls_g(fname, "code/Q4.py", caller, callee)

@E.evaluate
def eval_add_list_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.add_lists(l1, l2)
  ref = lambda: Ref.add_lists(l1, l2)
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_add_matrices_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.add_matrices(m1, m2)
  ref = lambda: Ref.add_matrices(m1, m2)
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_add_matrices_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name
  caller = "add_matrices"
  callee = "are_addable"
  return E.eval_f_calls_g(fname, "code/Q4.py", caller, callee)

@E.evaluate
def eval_add_matrices_3():
  fname = __name__ + "." + sys._getframe().f_code.co_name
  caller = "add_matrices"
  callee = "add_lists"
  return E.eval_f_calls_g(fname, "code/Q4.py", caller, callee)

@E.evaluate
def eval_multiply_lists_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.multiply_lists(l1, l2)
  ref = lambda: Ref.multiply_lists(l1, l2)
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_multiply_matrices_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.multiply_matrices(m1, m2)
  ref = lambda: Ref.multiply_matrices(m1, m2)
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_multiply_matrices_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q4 as Sub
  from mycode import matrix as Ref
  sub = lambda: Sub.multiply_matrices(m1, m2)
  ref = lambda: Ref.multiply_matrices(m1, m2)
  return E.eval_matfun(fname, sub, ref)

@E.evaluate
def eval_multiply_matrices_3():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  caller = "multiply_matrices"
  callee = "are_multipliable"
  return E.eval_f_calls_g(fname, "code/Q4.py", caller, callee)

@E.evaluate
def eval_multiply_matrices_4():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  caller = "multiply_matrices"
  callee = "transpose"
  return E.eval_f_calls_g(fname, "code/Q4.py", caller, callee)
  
@E.evaluate
def eval_multiply_matrices_5():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  caller = "multiply_matrices"
  callee = "multiply_lists"
  return E.eval_f_calls_g(fname, "code/Q4.py", caller, callee)
   
@E.evaluate
def eval_multiply_matrices_6():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  caller = "multiply_matrices"
  callee = "sum_of_list"
  return E.eval_f_calls_g(fname, "code/Q4.py", caller, callee)

tests = [
  (eval_is_wellformed_1, 1),
  (eval_is_wellformed_2, 1),
  (eval_is_wellformed_3, 1),
  (eval_is_wellformed_4, 1),
  (eval_are_addable_1, 1),
  (eval_are_addable_2, 1),
  (eval_are_addable_3, 1),
  (eval_are_addable_4, 1),
  (eval_are_addable_5, 1),
  (eval_are_addable_6, 2),
  (eval_are_multipliable_1, 1),
  (eval_are_multipliable_2, 1),
  (eval_are_multipliable_3, 1),
  (eval_are_multipliable_4, 1),
  (eval_are_multipliable_5, 1),
  (eval_are_multipliable_6, 1),
  (eval_are_multipliable_7, 1),
  (eval_are_multipliable_8, 2),
  (eval_scalar_multiply_list_1, 2),
  (eval_scalar_multiply_matrix_1, 2),
  (eval_scalar_multiply_matrix_2, 2),
  (eval_add_list_1, 2),
  (eval_add_matrices_1, 2),
  (eval_add_matrices_2, 2),
  (eval_add_matrices_3, 2),
  (eval_multiply_lists_1, 2),
  (eval_multiply_matrices_1, 3),
  (eval_multiply_matrices_2, 2),
  (eval_multiply_matrices_3, 2),
  (eval_multiply_matrices_4, 2),
  (eval_multiply_matrices_5, 2),
  (eval_multiply_matrices_6, 2),
]

eval_tests = E.testsuite(
  tests = tests
)

if __name__ == "__main__":
  total = sum([m for (_, m) in tests])
  print("total marks = ", total)
  print(eval_tests())
