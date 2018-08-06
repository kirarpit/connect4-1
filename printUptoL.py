length = 7

def myFunc(s):
  if (not len(s) or int(s) <= int('4'*len(s))) and len(s) == length:
    print(s)
  if len(s) and len(s) == length:
    return
  for i in range(1, 7):
    myFunc(s + str(i))

myFunc("")
