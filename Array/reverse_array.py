# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

def reverse_arr(arr, n):
    start = 0
    end = n-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


arr = [1, 2, 3, 4, 5, 6]

reverse_arr(arr, len(arr))
print(arr)
