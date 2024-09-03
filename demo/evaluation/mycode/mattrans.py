def mattrans(m):
  t = []
  for i in range(len(m[0])):
    t.append([])
  for i in range(len(m[0])):
    for j in range(len(m)):
      t[i].append(m[j][i])
  return t

if __name__ == "__main__":
  m = [[1, 2]]
  print(mattrans(m))
  m = [[1, 2], [3, 4]]
  print(mattrans(m))
