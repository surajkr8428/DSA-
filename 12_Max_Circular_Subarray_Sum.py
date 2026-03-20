
def maxCircularSum(arr):
    # code here
    
    t = 0
    mx_end = mn_end = 0
    mx = float('-inf')
    mn = float('inf')
    
    for x in arr:
        mx_end = max(x, mx_end + x)
        mx = max(mx,mx_end)
        
        mn_end = min(x, mn_end + x)
        mn = min(mn, mn_end)
        
        t += x
        
    if mx < 0:
        return mx
        
    return max(mx, t - mn)


arr = [[8, -8, 9, -9, 10, -11, 12],[10, -3, -4, 7, 6, 5, -4, -1],[5, -2, 3, 4]]
for i in arr:
    print("Input: ",i)
    print("Output: ",maxCircularSum(i))