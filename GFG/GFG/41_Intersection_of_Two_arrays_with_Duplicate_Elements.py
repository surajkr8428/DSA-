def intersect(a, b):
    # code here
    
    la = len(a)
    lb = len(b)
    
    sa = set(a)
    sb = set(b)
    
    lst = []
    
    if la > lb:
        for i in sb:
            if i in sa:
                lst.append(i)
    
    else:
        for i in sa:
            if i in sb:
                lst.append(i)
                
    return lst


a = [1, 2, 1, 3, 1]; b = [3, 1, 3, 4, 1]
# a = [1, 1, 1]; b = [1, 1, 1, 1, 1]
# a = [1, 2, 3]; b = [4, 5, 6]
print("Input: ",a,b)
print("Output: ",intersect(a, b))