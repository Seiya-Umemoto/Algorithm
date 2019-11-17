def getSolutionMatrix(O):
    S = []
    for i in range(len(O)):
        S.append([])
    for i in range(len(O)):
        for j in range(len(O[i])):
            if i == 0 and j == 0:
                S[i].append(O[i][j])
            elif j ==0:
                S[i].append(O[i][j] + S[i - 1][j])
            elif i ==0:
                S[i].append(O[i][j] + S[i][j-1])
            else:
                S[i].append(O[i][j] + max(S[i-1][j], S[i][j-1]))
    return S
def getHighestRoot(S, i, j, h_path):
    h_path.append(S[i][j])
    if i == 0 and j == 0:
        return h_path
    if 1 <= i < len(S) and 1 <= j < len(S[i]):
        if S[i][j - 1] > S[i - 1][j]:
            return getHighestRoot(S, i, j-1, h_path)
        else:
            return getHighestRoot(S, i - 1, j, h_path)
    elif i == 0:
        return getHighestRoot(S, i, j - 1, h_path)
    elif j == 0:
        return getHighestRoot(S, i - 1, j, h_path)
        
O = [[6, 7, 12, 5],
     [5, 3, 11, 18],
     [7, 17, 3, 3],
     [8, 10, 14, 9]]
S = getSolutionMatrix(O)
print(S)
path = []
path = getHighestRoot(S, len(S)-1, len(S[0])-1, path)
path.reverse()
print(path)