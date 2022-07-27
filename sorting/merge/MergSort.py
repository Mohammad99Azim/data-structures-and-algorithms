def merg(left, right, arr):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    if i >= len(left):
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    else:
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1


def mergesort(arr):
    if len(arr) > 1:
        m =len(arr) // 2
        left = arr[0:m]
        right = arr[m:]

        mergesort(left)

        mergesort(right)

        merg(left, right, arr)

    return arr

if __name__ == "__main__":
    # left = [1, 5, 7, 9]
    # right = [2, 3, 5, 8]
    # arr = [1, 5, 7, 9, 2, 3, 5, 8]
    arr = [8,4,23,42,16,15]
    mergesort(arr)

    print(arr)
