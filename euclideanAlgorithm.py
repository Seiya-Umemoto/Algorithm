def euclideanAlgorithm(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        euclideanAlgorithm(b, a%b)

print(euclideanAlgorithm(78696,19332))