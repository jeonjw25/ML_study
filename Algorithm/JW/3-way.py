#How to use:
# Initiate an array with any name and call function 'merge_sort' that takes array as an input, start as 1 and end as length of array.


def merge(arr, start, mid1, mid2, end):

    left_array = arr[start -1 : mid1]
    print('left_array : {0}'.format(left_array))
    mid_array = arr[mid1: mid2 + 1]
    print('mid_array : {0}'.format(mid_array))
    right_array = arr[mid2 + 1 : end]
    print('right_array : {0}'.format(right_array))

    left_array.append(float('inf'))
    mid_array.append(float('inf'))
    right_array.append(float('inf'))
    
    ind_left = 0
    ind_mid = 0
    ind_right = 0
    for i in range(start-1, end):
        minimum = min([left_array[ind_left], mid_array[ind_mid], right_array[ind_right]])
        if minimum == left_array[ind_left]:
            arr[i] = left_array[ind_left]
            ind_left += 1
        elif minimum == mid_array[ind_mid]:
            arr[i] = mid_array[ind_mid]
            ind_mid += 1
        else:
            arr[i] = right_array[ind_right]
            ind_right += 1
        print('arr : {0}'.format(arr))
            
def merge_sort(arr, start, end):

    if len(arr[start -1: end]) < 2:
        print('len(arr[start -1: end]) : {0}'.format(len(arr[start -1: end])))
        return arr
    else: 
        mid1 = start + ((end - start) // 3)
        print('mid1 : {0}'.format(mid1))
        mid2 = start + 2 * ((end-start) // 3)
        print('mid2 : {0}'.format(mid2))

        merge_sort(arr, start, mid1)
        merge_sort(arr, mid1+1, mid2 + 1)
        merge_sort(arr, mid2+2, end)
        merge(arr, start, mid1, mid2, end)
        return arr
    
arr = [312,413,3,423,5,3,342,1,2,53]
# arr = [6,5,4,3,2,1]
start = 1 #Start is 1, to comprise with code errors while dividing the array
end = len(arr) #length of array
print(merge_sort(arr, start, end))