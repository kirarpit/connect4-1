import os, pickle, time

start = time.time()
WIDTH = 6
fname = 'out'
sols = {}

def saveDict(sols):
  with open('dict', 'wb') as handle:
    pickle.dump(sols, handle, protocol=pickle.HIGHEST_PROTOCOL)

def mirror(e):
  j = ""
  for i in e:
    j += str(WIDTH + 1 - int(i))
  return j

def getBestMoves(moves):
    choices = []
    maxi = float("-inf")
    for index, value in enumerate(moves):
        if maxi <= value:
            if maxi<value:
                choices = [index]
                maxi = value
            else:
                choices.append(index)
    
    return choices

if os.path.exists(fname):
  with open(fname) as f:
    content = f.readlines()
  for x in content:
    line = x.split()
    sols[line[0]] = int(line[1])
    sols[mirror(line[0])] = int(line[1])
    
md = {}
def myFunc(sttr):
  if sttr in sols: return int(sols[sttr])#makes sure there is no missing 5 digit string's value

  scores = []
  for i in range(1, WIDTH + 1):
    value = myFunc(sttr + str(i))
    scores.append(-1 * value)

  md[(sttr,)] = getBestMoves(scores)
  return max(scores)

myFunc("")
saveDict(md)
print("Time taken: " + str(time.time() - start))
