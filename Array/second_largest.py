###
'''
Input: arr[] = {12, 35, 1, 10, 34, 1}
Output: The second largest element is 34.
Explanation: The largest element of the
array is 35 and the second
largest element is 34

Input: arr[] = {10, 5, 10}
Output: The second largest element is 5.
Explanation: The largest element of
the array is 10 and the second
largest element is 5

Input: arr[] = {10, 10, 10}
Output: The second largest does not exist.
Explanation: Largest element of the array
is 10 there is no second-largest element
'''

###

# O(nlogn)
# arr.sort


# o(n)

# def print_sec_largest(arr, n):

#     if n < 2:
#         print("Invalid input")
#         return
#     first = second = -1
#     for i in range(n):
#         first = max(first, arr[i])

#     for i in range(n):
#         if arr[i] != first:
#             second = max(second, arr[i])

#     if second == -1:
#         print("No second largest element found")
#     else:
#         print("Second largest element: ", second)


# one traversal
def print_sec_largest(arr, n):

    if n < 2:
        print("Invalid input")
        return
    first = second = -1
    for i in range(n):
        if(arr[i] > first):
            second = first
            first = arr[i]

        elif (arr[i] > second and arr[i] != first):
            second = arr[i]

    if (second == -2147483648):
        print("There is no second largest element")
    else:
        print("The second largest element is", second)


if __name__ == '__main__':

    arr = [12, 35, 100, 10, 37, 1]
    n = len(arr)
    print_sec_largest(arr, n)
