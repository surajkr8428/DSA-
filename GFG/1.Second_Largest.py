def Second_Largest(arr):
    
    arr.sort()
    m = arr.count(max(arr))
    
    if len(arr) == m:
        return -1
    
    else:
        for _ in range(m):
            arr.remove(max(arr))
            
        return max(arr)



ar = [[12, 35, 1, 10, 34, 1],[10, 5, 10],[10, 10, 10]]
for i in ar:
    print(Second_Largest(i))