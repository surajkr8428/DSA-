def reverseArray(arr):
    
    n = len(arr)
    l = [0]*n
    
    for i in range(n):
        l[i] = arr[n-i-1]
    
    for j in range(n):
        arr[j] = l[j]

    return arr
    
    
arr = [[1, 4, 3, 2, 6, 5],[4, 5, 2],[1]]

for i in arr:
    print(reverseArray(i))