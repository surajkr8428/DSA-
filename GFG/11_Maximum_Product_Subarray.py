
def maxProduct(arr):
    # code here
    
    mx_end = arr[0]
    mn_end = arr[0]
    mx = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < 0:
            mx_end, mn_end = mn_end,mx_end
            
        mx_end = max(arr[i],mx_end * arr[i])
        mn_end = min(arr[i],mn_end * arr[i])
        mx = max(mx,mx_end)
    
    return mx


arr = [[-2, 6, -3, -10, 0, 2],[-1, -3, -10, 0, 6],[2, 3, 4]]
for i in arr:
    print("Input: ",i)
    print("Output: ",maxProduct(i))