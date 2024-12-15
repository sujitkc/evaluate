import subprocess
import functools
import sys
import ast
import threading
import time
import io

mypython = "python3"

def equals(x, y):
  tx = type(x)
  ty = type(y)
  if((tx == int or tx == float) and (ty == int or ty == float)):
    return (abs(x - y) < 1.0)
  if(tx != ty):
    return False
  if(tx == list and ty == list):
    if(len(x) != len(y)):
      return False
    z = zip(x, y)
    tfs = [equals(a, b) for a, b in z]
    return functools.reduce(lambda a, b: a and b, tfs, True)
  elif(tx == tuple and ty == tuple):
    if(len(x) != len(y)):
      return False
    z = zip(x, y)
    for a, b in z:
      if(equals(a, b) == False):
        return False
    return True
  else:
    return x == y

def safe(f):
  def g():
    try:
      return f()
    except (
        KeyError,
        SyntaxError,
        NameError,
        AttributeError,
        TypeError,
        ImportError,
        IndexError,
        subprocess.CalledProcessError,
        UnboundLocalError,
        KeyboardInterrupt,
        ZeroDivisionError,
        FileNotFoundError,
        RecursionError,
        ValueError) as e:
      print("Exception raised: " + str(e))
      return (0, f.__name__ + ": " + str(e))
  return g

class MyThread(threading.Thread):
  def __init__(self, f):
    threading.Thread.__init__(self)
    self.f = f
    self.result = None

  def run(self):
    self.result = self.f()

def evaluate(f):
  safef = safe(f)
  
  def make_daemon():
    t = MyThread(f=safef)
    t.daemon = True
    t.start()
    timeout = True
    for i in range(10):
      if(t.is_alive()):
        time.sleep(0.1)
      else:
        return t.result
    return (0, f.__name__ + ": Timeout")
  return make_daemon

def testsuite(tests):
  def eval_tests():
    result = []
    result = [f() for (f, _) in tests]
    weights = [w for (_, w) in tests]
    test_results = [tr for (tr, _) in result]
    res_w = zip(test_results, weights)
    test_marks = [r * w for (r, w) in res_w]
    marks = sum(test_marks) 
    success_rate = marks / sum(weights)
    return (success_rate, result)

  return eval_tests

def evaluator(evals):
  def eval_all():

    marks = []
    for (test, qm) in evals:
      success_rate, result = test()
      individual_test_results = [m for (m, _) in result]
      print(individual_test_results)
      marks.append(success_rate * qm)
    return marks

  return eval_all

# compares the value 
def eval_value(fname, o, e):
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

def stub(f):
#  fname = sys._getframe().f_code.co_name
  return lambda: (1, f.__name__ + " : not tested.")

# compares the value returned by the mathematical function
def eval_matfun(fname, sub, ref):
  o = sub()
  e = ref()
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

# compares the value returned by the mathematical function that takes input
# from stdin
def eval_matfun_stdin(fname, inp, sub, ref):
  sys.stdin = io.StringIO(inp)
  o = sub()
  sys.stdin = sys.__stdin__

  sys.stdin = io.StringIO(inp)
  e = ref()
  sys.stdin = sys.__stdin__

  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

# compares the string printed on the standard output by the evaluated program
# Tested entity:     program under test (Python file)
# Calling mechanism: direct
# Input source:      standard input
# Output on:         standard output
def eval_program_stdin_stdout(fname, inp, filename):
  command = [mypython, "code/" + filename + ".py"]
  subprocess_obj = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  subprocess_obj.stdin.write(inp)
  o, error = subprocess_obj.communicate()
  subprocess_obj.stdin.close()
  command = [mypython, "mycode/" + filename + ".py"]
  subprocess_obj = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  subprocess_obj.stdin.write(inp)
  e, error = subprocess_obj.communicate()
  subprocess_obj.stdin.close()
 
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")


# compares the string printed on the standard output by the evaluated program
# with a separate driver.
# Tested entity:     program under test (Python file)
# Calling mechanism: through driver
# Input source:      None
# Output on:         standard output
def eval_named_proc_1(fname, driver):
  subprocess.call(["cp", "drivers/" + driver, "code/"])
  o = subprocess.check_output([mypython, "code/" + driver])
  e = subprocess.check_output([mypython, "mycode/" + driver])
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

# Contraption to capture the standard output from a called function
# Source: https://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call
from io import StringIO 

class Output(list):
  def __enter__(self):
    self._stdout = sys.stdout
    sys.stdout = self._stringio = StringIO()
    return self
  def __exit__(self, *args):
    self.extend(self._stringio.getvalue().splitlines())
    del self._stringio    # free up some memory
    sys.stdout = self._stdout

# compares the string printed to the standard output by a function
def eval_named_proc_2(fname, sub, ref):
  with Output() as o:
    sub()
  with Output() as e:
    ref()
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

# finds out if a function named caller is present in the filename which calls
#  another function callee.
def f_calls_g(filename, caller, callee):
  with open(filename, "r") as fin:
    tree = ast.parse(fin.read())
  for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef) and node.name == caller:
      body = node.body
      for s in body:
        for n in ast.walk(s):
          if(isinstance(n, ast.Call)):
            if isinstance(n.func, ast.Name) and n.func.id == callee:
              return True
            elif isinstance(n.func, ast.Attribute) and n.func.attr == callee:
              return True
  return False

def eval_f_calls_g(fname, filename, caller, callee):
  if(f_calls_g(filename, caller, callee)):
    return (1, fname)
  else:
    return(0, fname + ": " + caller + " doesn't call " + callee + ".")

# finds out if a function named f is present in the filename which
# is recursive
def is_recursive(filename, f):
  return f_calls_g(filename, f, f)

def eval_is_recursive(fname, filename, f):
  if(is_recursive(filename, f)):
    return (1, fname)
  else:
    return(0, fname + ": " + f + " is not recursive.")

# find out if a function named f uses list comprehension anywhere inside.
def has_list_comprehension(filename, f):
  with open(filename, "r") as fin:
    tree = ast.parse(fin.read())
  for node in ast.walk(tree):
    if isinstance(node, ast.ListComp):
      return True
  return False

def eval_has_list_comprehension(fname, filename, f):
  if(has_list_comprehension(filename, f)):
    return (1, fname)
  else:
    return(0, fname + ": " + f + " has no list comprehension.")

def get_all_inner_functions(filename, outer):
  with open(filename, "r") as fin:
    tree = ast.parse(fin.read())
  inner_functions = []
  for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef) and node.name == outer:
      body = node.body
      for s in body:
        for n in ast.walk(s):
          if isinstance(n, ast.FunctionDef):
            inner_functions.append(n.name)
  return inner_functions

# finds out if a function named 'inner' is an inner function in another
# function named 'outer'
def is_inner_function(filename, outer, inner):
  return inner in get_all_inner_functions(filename, outer)

def returns_name(filename, f, name):
  with open(filename, "r") as fin:
    tree = ast.parse(fin.read())
  for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef) and node.name == f:
      body = node.body
      for s in body:
        for n in ast.walk(s):
          if isinstance(n, ast.Return):
            if isinstance(n.value, ast.Name) and n.value.id == name:
                return True

  return False

def eval_is_inner_function(fname, filename, outer, inner):
  if(is_inner_function(filename, outer, inner)):
    return (1, fname)
  else:
    return(0, fname + ": " + f + " has no list comprehension.")

def get_arguments(filename, f):
  with open(filename, "r") as fin:
    tree = ast.parse(fin.read())
  for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef) and node.name == f:
      args = node.args.args
      return [arg.arg for arg in args]

# finds out the number of class definitions in the file name.
def num_of_classdefs(filename):
  with open(filename, "r") as fin:
    tree = ast.parse(fin.read())
  n = 0
  for node in ast.walk(tree):
    if isinstance(node, ast.ClassDef):
      n += 1
  return n

# finds out if there is a class definition of the given name in the file name.
def is_classdef(classname, filename):
  with open(filename, "r") as fin:
    tree = ast.parse(fin.read())
  for node in ast.walk(tree):
    if(isinstance(node, ast.ClassDef) and node.name == classname):
      return True
  return False

def eval_is_classdef(fname, filename, classname):
  if(is_classdef(classname, filename)):
    return (1, fname)
  else:
    return(0, fname + ": " + f + " has no class definition '" + classname + "'.")

# finds out if there is a method named 'functionname' in a class named 
# 'classname' in file named 'filename'.
def is_method(functionname, classname, filename):
  with open(filename, "r") as fin:
    tree = ast.parse(fin.read())
  for node in ast.walk(tree):
    if(isinstance(node, ast.ClassDef) and node.name == classname):
      for node1 in ast.walk(node):
        if(isinstance(node1, ast.FunctionDef) and node1.name == functionname):
          return True
      return False
  return False

def eval_is_method(fname, filename, classname, methodname):
  if(is_method(methodname, classname, filename)):
    return (1, fname)
  else:
    return(0, fname + ": '" + classname  + "' has no method named '" + methodname + "'.")

# finds the number of methods in the class 'classname' in the file named
# 'filename'.
def num_of_methods(classname, filename):
  with open(filename, "r") as fin:
    tree = ast.parse(fin.read())
  for node in ast.walk(tree):
    if(isinstance(node, ast.ClassDef) and node.name == classname):
      n = 0
      for node1 in ast.walk(node):
        if(isinstance(node1, ast.FunctionDef)):
          n += 1
      return n
  raise Exception("Class named '" + classname + "' not found in file '" + filename +".") 
