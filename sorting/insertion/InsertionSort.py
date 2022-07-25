
def InsertionSort(arr):
    for x in range(1, len(arr)):
        temp = arr[x]
        j = x - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

    return arr


if __name__ == "__main__":
    print(InsertionSort([8, 4, 23, 42, 16, 15]))
