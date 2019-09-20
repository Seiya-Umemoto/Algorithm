import random
import time

n = 10000

def insertion_sort(array):
    for i in range(1, len(array)):
        newMember = array[i]
        tailIndex = i-1
        while tailIndex>=0 and newMember < array[tailIndex]:
            array[tailIndex+1] = array[tailIndex]
            tailIndex = tailIndex-1
        array[tailIndex+1] = newMember
    return array

unordered = []
for i in range(0, n):
    num = random.randint(0, n)
    unordered.append(num)

start = time.time()
insertion_sort(unordered)
end = time.time()
res = end-start

if __name__ == "__main__":
    print(res)