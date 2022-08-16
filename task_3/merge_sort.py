def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        array_left = array[:mid]
        array_right = array[mid:]
        merge_sort(array_left)
        merge_sort(array_right)
        i = j = k = 0
        while i < len(array_left) and j < len(array_right):
            if array_left[i] < array_right[j]:
                array[k] = array_left[i]
                i += 1
            else:
                array[k] = array_right[j]
                j += 1
            k += 1
        while i < len(array_left):
            array[k] = array_left[i]
            i += 1
            k += 1
        while j < len(array_right):
            array[k] = array_right[j]
            j += 1
            k += 1
    elif len(array) == 1:
        pass
    else:
        print('Array is Empty')


arr = [1, 0, -1, 1, 10, 0.2, 1, 43,432, 234,234 ,23423,4234,234,23,42,34]
merge_sort(arr)
print(arr)
