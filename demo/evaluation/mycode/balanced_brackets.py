def balanced_brackets(s):
  paren = 0
  brace = 0
  square = 0

  for c in s:
    if c == "(": paren += 1
    if c == "{": brace += 1
    if c == "[": square += 1
    if c == ")": paren -= 1
    if c == "}": brace -= 1
    if c == "]": square -= 1

    if(paren < 0 or brace < 0 or square < 0): return False

  if(paren != 0 or brace != 0 or square != 0): return False
  else: return True

if __name__ == "__main__":
  print(balanced_brackets("()"))
  print(balanced_brackets(")"))
