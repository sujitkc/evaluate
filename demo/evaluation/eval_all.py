#!/usr/bin/python3
import sys
sys.path.append("/home/sujit/IIITB/projects/evaluate/evaluate/")

import evaluate

import eval_sop
import eval_mathop
import eval_matrices
import eval_print_message_a
import eval_print_message_b
import eval_print_message_c
import eval_print_message_d
import eval_banner
import eval_diamond_a
import eval_diamond_b
import eval_diamond_c
import eval_ndiamond_a
import eval_ndiamond_b
import eval_hello
import eval_double
import eval_even_elements
import eval_balanced_brackets
import eval_mattrans
import eval_matmul


eval_all = evaluate.evaluator(
  evals = [
    (eval_sop.eval_tests, 10),
    (eval_mathop.eval_tests, 17),
    (eval_matrices.eval_tests, 49),
    (eval_print_message_a.eval_tests, 1),
    (eval_print_message_b.eval_tests, 1),
    (eval_print_message_c.eval_tests, 1),
    (eval_print_message_d.eval_tests, 1),
    (eval_banner.eval_tests,  1),
    (eval_diamond_a.eval_tests, 1),
    (eval_diamond_b.eval_tests, 1),
    (eval_diamond_c.eval_tests, 1),
    (eval_ndiamond_a.eval_tests, 1),
    (eval_ndiamond_b.eval_tests, 1),
    (eval_hello.eval_tests, 1),
    (eval_double.eval_tests, 1),
    (eval_even_elements.eval_tests, 3),
    (eval_balanced_brackets.eval_tests, 6),
    (eval_mattrans.eval_tests, 10),
    (eval_matmul.eval_tests, 10),
  ])

if __name__ == "__main__":
  if(len(sys.argv) > 1):
    roll_number = sys.argv[1]
  else:
    roll_number = ""
  marks = eval_all()
  total = sum(marks)
  print(roll_number + " marks = " + str(marks) + " total = " + str(total))
