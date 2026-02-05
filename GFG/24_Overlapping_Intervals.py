
def mergeOverlap(arr):
    # Code here
        
    arr.sort(key = lambda x:x[0])
    
    merged = []
    result = []
    
    s,e = arr[0]
    
    for i in range(1,len(arr)):
        if arr [i][0] <= e:
            e = max(e, arr[i][1])
        else:
            result.append([s,e])
            s,e = arr[i]
            
    result.append([s,e])
    return result

	
l = [[1, 3], [2, 4], [6, 8], [9, 10]]	
# l = [[6, 8], [1, 9], [2, 4], [4, 7]]

print("Input: ",l)
print("Output: ",mergeOverlap(l))

