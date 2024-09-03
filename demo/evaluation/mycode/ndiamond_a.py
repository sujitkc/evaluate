def ndiamond_n(n):
  lst1 = []
  for i in range(0, int(n / 2) + 1):
    spaces = ' ' * int((n / 2) - i)
    num_cs = 2 * i + 1
    cs1 = ""
    for j in range(1, int((num_cs + 3) / 2)):
      cs1 += str(j)
    cs2 = cs1[::-1]
    cs2 = cs2[1:]
    row = spaces + cs1 + cs2
    lst1.append(row)
  lst2 = lst1[::-1]
  lst2 = lst2[1:]
  lst = lst1 + lst2

  for row in lst:
    print(row)

def ndiamond():
  ndiamond_n(5)

if __name__ == "__main__":
  ndiamond()
