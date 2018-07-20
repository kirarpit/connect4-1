def myFunc(s):
  if (not len(s) or int(s) <= int('4'*len(s))) and len(s) == 5:
    print(s)
  if len(s) and len(s) == 5:
    return
  for i in range(1, 8):
    myFunc(s + str(i))

myFunc("")
