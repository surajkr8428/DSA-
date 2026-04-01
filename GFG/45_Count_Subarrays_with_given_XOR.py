def subarrayXor(arr, k):
    # code here
    
    x = 0
    f = {0: 1}
    c = 0
    
    for n in arr:
        x ^= n
        
        if (x^k) in f:
            c += f[x ^ k]
            
        f[x] = f.get(x,0) + 1
        
    return c

arr = [4, 2, 2, 6, 4]; k = 6
# arr = [5, 6, 7, 8, 9] k = 5
# arr = [1, 1, 1, 1]; k = 0

print("input: ","arr: ",arr,"k: ", k)
print("output: ",subarrayXor([5, 6, 7, 8, 9], 5))