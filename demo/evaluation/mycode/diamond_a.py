def diamond_n(n):
  for i in range(0, int(n / 2)):
    spaces = ' ' * int((n / 2) - i)
    cs = '*' * (2 * i + 1)
    row = spaces + cs
    print(row)
  print('*' * n)
  for i in range(int(n / 2) - 1, -1, -1):
    spaces = ' ' * int((n / 2) - i)
    cs = '*' * (2 * i + 1)
    row = spaces + cs
    print(row)

def diamond():
  diamond_n(5)
if __name__ == "__main__":
  diamond()
