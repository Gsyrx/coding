# Input: arr[] = {10, 20, 4}
# Output: 20

# Input: arr[] = {20, 10, 20, 4, 100}
# Output: 100


def largest(arr, n):

    maxi = arr[0]

    for i in range(n):
        if arr[i] > maxi:
            maxi = arr[i]
    return maxi


if __name__ == '__main__':
    arr = [10, 324, 45, 90, 9808]
    n = len(arr)

    ans = largest(arr, n)

    print("Largest in given array is", ans)
