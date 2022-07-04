a = [12, 11, 13, 5, 6]

#Python Bubble Sort

def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if(arr[j] < arr[j-1]):
                x = arr[j]
                arr[j] = arr[j -1]
                arr[j-1] = x
    return a

print(BubbleSort(a))