def bubble_sort(array):
    for i in range(0, len(array)-1):
        flag = True
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                flag = False
        if flag == True:
            break
    return array
array = [3, 5, 6, 7, 2]
print(bubble_sort(array))