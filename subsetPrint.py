def subsetPrint(given_array, subset, depth):
    if depth == len(given_array):
        print(subset)
    else:
        subsetPrint(given_array, subset, depth + 1)
        subset.append(given_array[depth])
        subsetPrint(given_array, subset, depth + 1)
        subset.pop()

given_array = ["a", "b", "c"]
subset= []
subsetPrint(given_array, subset, 0)