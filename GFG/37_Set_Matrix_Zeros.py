def setMatrixZeroes(mat):
    # code here
    
    r = []
    c = []
        
    r_n = len(mat)
    c_n = len(mat[0])
    
    for i in range(r_n):
        for j in range(c_n):
            if mat[i][j] == 0:
                r.append(i)
                c.append(j)
    
    
    for a in r:
        for b in range(c_n):
            mat[a][b] = 0
    
    for c1 in range(r_n):
        for d in c:
            mat[c1][d] = 0
            
    return mat


mat = [[1,-1,1],[-1,0,1],[1,-1,1]]
print("Input: ",mat)
print("Output: ",setMatrixZeroes(mat))