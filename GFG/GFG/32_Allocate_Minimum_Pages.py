def findPages(arr, k):
    # code here
    
    n = len(arr)
    
    if k > n:
        return -1
        
    low = max(arr)
    high = sum(arr)
    
    
    while low <= high:
        mid = (low + high) // 2
        
        s = 1
        c_s = 0
        
        for p in arr:
            if c_s + p > mid:
                s += 1
                c_s = p
            else:
                c_s += p
        
        if s <= k:
            high = mid - 1
        else:
            low = mid + 1
            
    return low


arr = [12, 34, 67, 90]; k = 2
# arr = [15, 17, 20]; k = 5

print("Input: ",arr,k)
print("Output: ",findPages(arr, k))