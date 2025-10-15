def rotateArr(arr, d):
    
    n = len(arr)
    # l = [0]*n
    l = []
    
    for i in range(d,n):
        l.append(arr[i])
    
    for j in range(d):
        # l.append(arr[j])
        pass
    
    for k in range(n):
        arr[k] = l[k]
    
ip1 = [[1, 2, 3, 4, 5],2]
ip2 = [[2, 4, 6, 8, 10, 12, 14, 16, 18, 20],3]
ip3 = [[7, 3, 9, 1],9]

ip = [ip1,ip2,ip3]

for a in ip:
    print(a[0],a[1])
    print(rotateArr(a[0],a[1]))