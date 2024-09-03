import sys

# Well-formedness specification:
# * Number of rows should not be zero
# * All rows should be of the same length.
# * Rows shouldn't be empty.
def is_wellformed(m):
  if(len(m) == 0):
    return False
  for i in range(1, len(m)):
    if(len(m[i]) != len(m[0])):
      return False
  if(len(m[0]) == 0):
    return False
  return True

# Addability specifications:
# * Well-formed matrix: Each row should be of the same length.
# * Both matrices should have the same number of rows.
# * Each corresponding row of both matrices should be of equal length.
def are_addable(m1, m2):
  if(not (is_wellformed(m1) and is_wellformed(m2))):
    return False
  if(len(m1) != len(m2)):
    return False
  if(len(m1[0]) != len(m2[0])):
    return False
  return True

# Multipliability specifications:
# * Well-formed matrix
# * The number of columns in m1 should be equal to the number of rows in m2.
def are_multipliable(m1, m2):
  if(not (is_wellformed(m1) and is_wellformed(m2))):
    return False
  if(len(m1[0]) != len(m2)):
    return False
  return True

def scalar_multiply_list(n, l):
  return [n * e for e in l]

def scalar_multiply_matrix(n, m):
  return [scalar_multiply_list(n, row) for row in m]

def add_lists(l1, l2):
  if(len(l1) != len(l2)):
    print("add_lists: input lists of unequal length.")
    sys.exit(0)
  return [l1[i] + l2[i] for i in range(len(l1))]

def add_matrices(m1, m2):
  if(not are_addable(m1, m2)):
    print("add_matrices: Input matrices are not addable.")
  return [add_lists(m1[i], m2[i]) for i in range(len(m1))]

def multiply_lists(l1, l2):
  if(len(l1) != len(l2)):
    print("multiply_lists: input lists of unequal length.")
    sys.exit(0)
  return [l1[i] * l2[i] for i in range(len(l1))]

def transpose(m):
  t = []
  for i in range(len(m[0])):
    t.append([])
  for i in range(len(m[0])):
    for j in range(len(m)):
      t[i].append(m[j][i])
  return t

def multiply_matrices(m1, m2):
  if(not are_multipliable(m1, m2)):
    print("multiply_matrices: m1 and m2 are not multipliable.")
    sys.exit(0)
  t2 = transpose(m2)
  m = []
  for r in m1:
    row = []
    for c in t2:
      l = multiply_lists(r, c)
      row.append(sum(l))
    m.append(row)
  return m

################## test #######################################
def t_transpose_1():
  print(transpose([[1, 2, 3],[4, 5, 6]]))

def t_multiply_matrices_1():
  print(multiply_matrices([[1, 2, 3],[4, 5, 6]], [[7, 10], [8, 11], [9, 12]]))
  
def t_multiply_matrices_2():
  print(multiply_matrices([[1, 2],[4, 5]], [[7, 10], [8, 11], [9, 12]]))

if __name__ == "__main__":
  t_transpose_1()
  t_multiply_matrices_1()
  t_multiply_matrices_2()
