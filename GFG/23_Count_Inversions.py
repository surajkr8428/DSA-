def inversionCount(arr):
    # Code Here
    
    def sort(l,r):
        if l >= r:
            return 0
        
        m = (l + r) // 2
        inv = sort(l,m) + sort(m + 1, r)
        
        
        temp, i, j = [], l, m + 1
        
        while i <= m and j <= r:
            
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            
            else:
                temp.append(arr[j])
                inv += m - i + 1
                j += 1
                
        temp += arr[i:m+1] + arr[j:r+1]
        arr[l:r+1] = temp
        
        return inv
        
    return sort(0,len(arr) - 1)


arr = [[2, 4, 1, 3, 5],[2, 3, 4, 5, 6],[10, 10, 10]]
for a in arr:
    print("Input: ",a)
    print("Output: ",inversionCount(a))