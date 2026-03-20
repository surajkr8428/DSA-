def countPairs(arr, target):
        #code here
        
        # c = 0
        # l = len(arr)
        # # print(target)
        
        # for i in range(l):
        #     for j in range(i,l):
                
        #         if i != j and arr[i] + arr[j] == target:
        #             c += 1
        
        # return c
        
        
        f = {}
        c = 0
        
        for n in arr:
            cm = target - n
            
            if cm in f:
                c += f[cm]
            
            f[n] = f.get(n,0) + 1
        
        return c
        

# arr = [1, 5, 7, -1, 5]; target = 6
arr = [6806, -3873, 6780, -8321, -181, -12, 789, -3146, 1885, -5697, -7730, 4545, 5370, -5290, 7611, -7673, 111, -5467, 6268, 5603, -3054, -7154, 6820, 9673, -7418, 5990, -4755, -5535, -2964, 9051, -2692, 503, -2141, -7489, 9735, -7897, 3244, -6166, -3332, -9960, 9771, 9586, -7147, 3272, 4970, -2402, -1110, -6075,
 4789]; target = 4296
print("Input: ",arr,target)
print("Output: ",countPairs(arr, target))

