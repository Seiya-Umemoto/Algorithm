def euclideanAlgorithm(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return euclideanAlgorithm(b, a%b)

print(euclideanAlgorithm(78696,19332))
print(euclideanAlgorithm(6, 36))
print(euclideanAlgorithm(36, 30))