def rotateMatrix(mat):
    # code here
    
    r = len(mat)
    c = len(mat[0])
    res = []
    
    for i in range(r-1,-1,-1):
        l = []
        for j in range(c):
            
            l.append(mat[j][i])
        res.append(l)
    
    for a in range(r):
        for b in range(c):
            mat[a][b] = res[a][b]
            
    return mat

mat = [[0, 1, 2], 
        [3, 4, 5], 
        [6, 7, 8]] 
print("Input: ",mat)
print("Output: ",rotateMatrix(mat))
        