import math

def insertion_sort(array):
    for i in range(1, len(array)):
        newMember = array[i]
        tailIndex = i-1
        while tailIndex>=0 and newMember < array[tailIndex]:
            array[tailIndex+1] = array[tailIndex]
            tailIndex = tailIndex-1
        array[tailIndex+1] = newMember
    return array

array1 = [math.log(3), math.log2(3), math.log10(4), math.log(4), math.log(3)]
print(insertion_sort(array1))