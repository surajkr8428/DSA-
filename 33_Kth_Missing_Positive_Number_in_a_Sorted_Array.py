def kthMissing(self, arr, k):
    # code here
    
    l,r = 0,len(arr)-1
    
    while l <= r:
        mid = (l + r) // 2
        m = arr[mid] - (mid + 1)
        
        if m < k:
            l = mid + 1
        else:
            r = mid - 1
    
    return l + k