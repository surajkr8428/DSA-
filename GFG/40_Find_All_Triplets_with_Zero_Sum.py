def findTriplets(self, arr):
        
    from collections import defaultdict
    i_m = defaultdict(list)
    
    r = []
    
    for j in range(len(arr)):
        for k in range(j + 1, len(arr)):
            t = -(arr[j] + arr[k])
            
            if t in i_m:
                for i in i_m[t]:
                    if i < j:
                        r.append([i,j,k])
                        
        i_m[arr[j]].append(j)
        
    return r

arr = [0, -1, 2, -3, 1]
# arr = [1, -2, 1, 0, 5]
# arr = [2, 3, 1, 0, 5]
print("Input: ",arr)
print("Output: ",findTriplets(arr))

