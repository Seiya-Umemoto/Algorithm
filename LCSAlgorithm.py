def makeList():
    c = []
    for i in range(len(X)+1):
        c.append([0])
    for i in range(1, len(Y)+1):
        c[0].append(0)
    return c

def createMatrix(c):
    for i in range(1,len(X)+1):
        for j in range(1, len(Y) + 1):
            if X[i-1]== Y[j-1]:
                c[i].append(c[i-1][j-1] + 1)
            else:
                c[i].append(max(c[i][j-1], c[i-1][j])) 
    return c

def findSubsetSequence(c, i, j, subset):
    if i == 0 or j == 0:
        print(subset)
        return subset
    if X[i-1] == Y[j-1]:
        subset.insert(0, X[i-1])
        return findSubsetSequence(c, i-1, j-1, subset), subset.pop(0)
    elif c[i-1][j] == c[i][j-1]:
        return findSubsetSequence(c, i-1, j, subset), findSubsetSequence(c, i, j-1, subset)
    elif c[i-1][j] > c[i][j-1] :
        return findSubsetSequence(c, i-1, j, subset)
    else:
        return findSubsetSequence(c, i, j-1, subset)

X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'A']
c = makeList()
c = createMatrix(c)
print(c[len(X)][len(Y)])
subset = []
findSubsetSequence(c, len(X), len(Y), subset)