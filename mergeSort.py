def mergeSort(A):
    left = []
    right = []
    if len(A) <= 1:
        return A
    else:
        middle = len(A)//2
        left = A[:middle]
        # for i in range(0, middle):
        #     left.append(A[i])
        right = A[middle:]
        # for i in range(middle, len(A)):
        #     right.append(A[i])
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result

import insertionSort
import random
import time

n = 10000

unordered = []
for i in range(0, n):
    num = random.randint(0, n)
    unordered.append(num)

start = time.time()
mergeSort(unordered)
end = time.time()
res2 = end-start

if __name__ == "__main__":
    print(f'The speed of processing {insertionSort.n} data with Insertion Sort:')
    print(insertionSort.res)
    print(f'The speed of processing {n} data with Merge Sort:')
    print(res2)
    print(f'It takes for Insertion Sort to process data {insertionSort.res/res2} times longer than Merge Sort does.')