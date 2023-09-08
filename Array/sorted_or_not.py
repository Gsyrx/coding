# Input: arr[] = {8, 12, 15}
# Output: Yes    // Since all elements are in ascending order

# Input: arr[] = {8, 10, 10, 12}
# Output: Yes    // Since all elements are in ascending order (elements may be repeated)


# Input: arr[] = {100, 20 ,200}
# Output: No     // Elements are not in ascending order

# Input: arr[] = {200, 100}
# Output: No     // Since we are checking an array to be sorted in ascending order

def arraySortedOrNot(arr, n):

    if (n == 0 or n == 1):
        return True

    for i in range(1, n):

        if (arr[i-1] > arr[i]):
            return False

    return True


arr = [20, 23, 23, 45, 78, 88]
n = len(arr)
if (arraySortedOrNot(arr, n)):
    print("Yes")
else:
    print("No")
