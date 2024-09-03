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

# Multipliability specifications:
# * Well-formed matrix
# * The number of columns in m1 should be equal to the number of rows in m2.
def are_multipliable(m1, m2):
  if(not (is_wellformed(m1) and is_wellformed(m2))):
    return False
  if(len(m1[0]) != len(m2)):
    return False
  return True

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

def matmul(m1, m2):
  if(not are_multipliable(m1, m2)):
    return "matmul: m1 and m2 are not multipliable."
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

def t_matmul_1():
  print(matmul([[1, 2, 3],[4, 5, 6]], [[7, 10], [8, 11], [9, 12]]))
  
def t_matmul_2():
  print(matmul([[1, 2],[4, 5]], [[7, 10], [8, 11], [9, 12]]))

if __name__ == "__main__":
  t_transpose_1()
  t_matmul_1()
  t_matmul_2()
