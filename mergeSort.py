def mergeSort(A):
    left = []
    right = []
    if len(A) <= 1:
        return A
    else:
        middle = len(A)//2
        for i in range(0, middle):
            left.append(A[i])
        for i in range(middle, len(A)):
            right.append(A[i])
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

print(f'{insertionSort.n}개의 데이터를 삽입정렬로 처리하는 속도:')
print(insertionSort.res)
print(f'{n}개의 데이터를 병합정렬로 처리하는 속도:')
print(res2)
print('삽입정렬의 처리속도는 병합정렬의 처리속도보다')
print(f'{insertionSort.res/res2}배 시간이 걸린다.')

