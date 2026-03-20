def mergeArrays(self, a, b):
    # code here
    
    n = len(a)
    m = len(b)
    
    gap = (n+m+1)//2
    
    while gap > 0:
        i = 0
        j = gap
        
        while j < n + m:
            if i < n and j < n:
                if a[i] > a[j]:
                    a[i], a[j] = a[j],a[i]
                    
            elif i < n and j >= n:
                if a[i] > b[j-n]:
                    a[i],b[j-n] = b[j-n],a[i]
            
            else:
                if b[i-n] > b[j-n]:
                    b[i-n], b[j-n] = b[j-n], b[i-n]
            
            i += 1
            j += 1
            
            
        if gap == 1:
            gap = 0
        else:
            gap = (gap + 1)//2
            
    return a, b


a = [2, 4, 7, 10]; b = [2, 3]
# a = [1, 5, 9, 10, 15, 20]; b = [2, 3, 8, 13]
# a = [0, 1]; b = [2, 3]

print("Input: ",a,b)
print("Output: ",mergeArrays(0, a, b))
