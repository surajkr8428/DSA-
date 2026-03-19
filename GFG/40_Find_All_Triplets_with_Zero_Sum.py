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