def PushZerosToEnd(arr):
    
    z = arr.count(0)
    for i in arr:
        if i == 0:
            arr.remove(i)
    
    for _ in range(z):
        arr.append(0)
        
    return arr
    
ar = [[1, 2, 0, 4, 3, 0, 5, 0],[10, 20, 30],[0, 0]]
for a in ar:
    print(PushZerosToEnd(a))
