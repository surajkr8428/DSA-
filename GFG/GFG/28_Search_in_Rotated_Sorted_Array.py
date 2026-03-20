def search(arr, key):
    # code here
    
    if key not in arr:
        return -1
        
    else:
        return arr.index(key)
    
    
arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
k = 3
# for i in arr:
print("Output: ",search(arr,k))