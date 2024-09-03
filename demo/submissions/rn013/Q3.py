def banner(m):
    i = 0
    for i in range(0, len(m)+3):  # printing the first row
        print("*", end = "")
    print("*")       #  printng the last asterisk of first row seperately in order to jump to new line
    print("* " + m + " *")      # printing the middle row
    i = 0
    for i in range(0, len(m) + 3):  # printing the last row
        print("*", end="")
    print("*")

