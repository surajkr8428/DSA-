def PushZerosToEnd(arr):
    
    # z = arr.count(0)
    # for i in arr:
    #     if i == 0:
    #         arr.remove(i)
    
    # for _ in range(z):
    #     arr.append(0)
        
    # return arr
    
    #User function Template for python3

    # def pushZerosToEnd(self,arr):
        # code here
        pos = 0
        
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[pos] = arr[i]
                pos += 1
                
        while pos < len(arr):
            arr[pos] = 0
            pos += 1
        
        return arr
        
    #     print(*arr)
        
    #     return a
    #     print("arr:",arr)
        # return "".join(map(str,arr))

    
ar = [[1, 2, 0, 4, 3, 0, 5, 0],[10, 20, 30],[0, 0]]
for a in ar:
    print(PushZerosToEnd(a))
