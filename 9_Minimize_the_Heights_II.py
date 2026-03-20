def getMinDiff(arr, k):
    # code here
    
    n = len(arr)
    arr.sort()
    ans = arr[n-1] - arr[0]
    s = arr[0] + k
    b = arr[n-1] - k
    
    for i in range(1,n):
        if arr[i] - k < 0:
            continue
        
        mn_h = min(s,arr[i] - k)
        mx_h = max(b,arr[i-1] + k)
        
        ans = min(ans, mx_h - mn_h)
        
    return ans

arr = {5:[1, 5, 8, 10],11:[3, 9, 12, 16, 20]}
for a,k in arr.items():
    print("Input: ",a,k)
    print(" Output: ",getMinDiff(a,k) )