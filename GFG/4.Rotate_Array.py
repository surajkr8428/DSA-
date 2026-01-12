def rotateArr(arr, d):
    #Your code here
    
    # l = len(arr)
    # t = [0]*l
    
    # if d == l:
    #     return arr
    
    # else:
    #     if d > l:
    #         d = d % l
        
    #     for i in range(l-d):
    #         # t.append(arr[i])
    #         t[i] = arr[d+i]
        
    #     for j in range(d):
    #         t[l-d+j] = arr[j]
            
    #     for a in range(l):
    #         arr[a] = t[a]
        
    #     return arr
    print("Original Array: ",arr)
    ln = len(arr)
    l = arr
    if d == ln:
        return arr
    elif d > ln:
        d = d % ln
        
    for a in range(d):
        arr.append(l[a])
    for i in range(d):
        arr.pop(0)
    return arr
    
ip1 = [[1, 2, 3, 4, 5],2]
ip2 = [[2, 4, 6, 8, 10, 12, 14, 16, 18, 20],3]
ip3 = [[7, 3, 9, 1],9]

# print(rotateArr([1, 2, 3, 4, 5],2))
ip = [ip1,ip2,ip3]

for a in ip:
    # print(a[0],a[1])
    # print(a[0],a[1])
    print("Rotated Array: ",rotateArr(a[0],a[1]))