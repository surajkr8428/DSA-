def maxSubarraySum(arr):
    # Code here
    
    cr_sum = arr[0]
    max_sum = arr[0]
    
    for i in range(1, len(arr)):
        cr_sum = max(arr[i], cr_sum + arr[i])
        max_sum = max(max_sum, cr_sum)
        
    
    return max_sum


arr = [[2, 3, -8, 7, -1, 2, 3],[-2, -4],[5, 4, 1, 7, 8]]
for i in arr:
    print("Input: ",i)
    print("Output: ",maxSubarraySum(i))