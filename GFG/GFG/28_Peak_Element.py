def peakElement(arr):
    # Code here
    
    # m = max(arr)
    i = arr.index(max(arr))
    
    n = len(arr)
    
    if i > 0 and i < n - 1:
        return i
    else:
        return i
    
    
    
arr = [[1, 2, 4, 5, 7, 8, 3],[10, 20, 15, 2, 23, 90, 80]]
for i in arr:
    print("Input: ",i)
    print("Output: ",peakElement(i))
