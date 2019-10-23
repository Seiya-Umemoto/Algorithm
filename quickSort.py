def quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)

        quick_sort(array, p, q-1)
        quick_sort(array, q+1, r)

def partition(array, p, r):
    q = p
    for i in range(p, r):
        if array[i] <= array[r]:
            array[q], array[i] = array[i], array[q]
            q += 1
    array[q], array[r] = array[r], array[q]
    return q

# array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
# quick_sort(array, 0, len(array)-1)
# print(array)

import mergeSort
import random
import time

n = 10000

unordered = []
for i in range(0, n):
    num = random.randint(0, n)
    unordered.append(num)

start = time.time()
quick_sort(unordered, 0, len(unordered)-1)
end = time.time()
res_q = end-start

if __name__ == "__main__":
    print(f'The speed of processing {mergeSort.n} data with Merge Sort:')
    print(mergeSort.res2)
    print(f'The speed of processing {n} data with Quick Sort:')
    print(res_q)
    print(f'It takes for Merge Sort to process data {mergeSort.res2/res_q} times longer than Quick Sort does.')