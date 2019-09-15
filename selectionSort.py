import math

def selection_sort(array):
    for border in range(0, len(array)-1):
        min = border
        for pointer in range(border+1,len(array)):
            if array[min] > array[pointer]:
                min = pointer # save pointer_index as var min
        temp = array[border]
        array[border] = array[min]
        array[min] = temp
    return array

array = [64, 25, 12, 22, 11]
print(selection_sort(array))

array2 = [4.5, -43.5, 0, 34, -2, 33]
print(selection_sort(array2))

array3 = [3.4, math.sqrt(4), 3, math.log(2.719), math.log(8,2)]
print(selection_sort(array3))