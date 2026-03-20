
def MatrixTraverse(mat):
    
    # print(mat)
    
    r = len(mat)   ## Number of rows
    c = len(mat[0])  ## Number of columns
    mat = [[0] * c for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            # print(0, end = " ")
            print(mat[i][j], end = " ")
            
        print()
        
    e = 1
    i, j = 0, 0
    
    while e <= r*c:
        if i == 0 and j < c:
            mat[i][j] = 1
            j += 1
        
        elif j == c and i < r:
            mat[i][j-1] = 1
            i += 1
        elif i == r-1 and j == c-1:
            mat[i][j] = 1
            j -= 1
            
        e += 1
            
    print("--------------------")    
    for i in range(r):
        for j in range(c):
            # print(0, end = " ")
            print(mat[i][j], end = " ")
            
        print()
    
    
    
    return 0


mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print("Input: ",mat)    
print("Output: ",MatrixTraverse(mat))