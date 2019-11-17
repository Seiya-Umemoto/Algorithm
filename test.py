def recursive(i, j):
    if i == 0 and j == 0:
        return "end"
    elif 1<=i <= 3:
        return recursive(i - 1, j)
    elif 1<=j <= 3:
        return recursive(i, j-1)

print(recursive(3, 3))