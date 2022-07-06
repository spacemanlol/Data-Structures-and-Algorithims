def merge_sort(arr):
    # Divide Array Into 2 Subpieces
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]


        # Recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Merge
        i = 0 # left idx
        j = 0 # right idx
        k = 0 # merge idx

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr

arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]

print(merge_sort(arr_test))