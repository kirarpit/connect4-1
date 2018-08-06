import os, pickle

fname = 'dict'
fname2 = '/Users/Arpit/DDQN/src/dicts/miniMax5X6Shell.pickle'

def saveDict(sols):
  with open('finalDict', 'wb') as handle:
    pickle.dump(sols, handle, protocol=pickle.HIGHEST_PROTOCOL)

def loadDict(dictName):
    if os.path.exists(dictName):
        with open(dictName, 'rb') as handle:
            return pickle.load(handle)

dict1 = loadDict(fname)
dict2 = loadDict(fname2)

for key, value in dict1.items():
    dict2[key] = value

saveDict(dict2)
