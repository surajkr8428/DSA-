def findMajority(arr):
        
    l = len(arr)
    f = l//3
    d = {}
    for i in arr:
        if i not in d.keys():
            d[i] = 1
        elif i in d.keys():
            d[i] += 1
    
    lst = []
    for a,b in d.items():
        if b > f:
            lst.append(a)
    
    return sorted(lst)


ls = [[2, 2, 3, 1, 3, 2, 1, 1],[-5, 3, -5],[3, 2, 2, 4, 1, 4]]
for i in ls:
    print("Input: ",i)
    print("Output :",findMajority(i))