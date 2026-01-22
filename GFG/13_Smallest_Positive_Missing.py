

def smallestMissingPositive(arr):
    n = len(arr)

    # Place each number in its correct position
    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
            correct = arr[i] - 1
            arr[i], arr[correct] = arr[correct], arr[i]

    # Find the first missing positive
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1

    return n + 1

arr = [[2, -3, 4, 1, 1, 7],[5, 3, 2, 5, 1],[-8, 0, -1, -4, -3]]