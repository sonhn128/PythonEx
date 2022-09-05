from random import sample
numLst = sample(range(1,100), 10)
print(numLst)
for i in range(0, len(numLst) - 1):
    for j in range(i+1, len(numLst)):
        if numLst[i] > numLst[j]:
            numLst[i], numLst[j] = numLst[j], numLst[i]
print(numLst)