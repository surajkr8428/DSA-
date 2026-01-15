# def nextPermutation(ar):
    
#     n = len(ar)  ## length of array
#     ## Finding Pivot Point
#     # for i in range(n-1):
#     #     if ar[i] > ar[i+1]:
#     #         p = i+1
#     #         break
#     p = -1
#     for i in range(n-2,-1,-1):
#         if ar[i] < ar[i+1]:
#             p = i
#             break
#     print("Pivot Element:",ar[p])
    
#     if p == -1:
#         return ar.reverse()
#     else:
#     ## Swaping pivot and Rightmost greater element
#         g = max(ar[p:n])
#         q = p
#         for j in range(p+1,n-1):
#             if ar[p-1] < ar[j] and ar[j] <= g:
#                 # ar[p],ar[j] = ar[j],ar[p]
#                 g = ar[j]
#                 q = j
#                 # break
            
#         ar[p],ar[q] = ar[q],ar[p]
#         print("Swaped Array:",ar)
#         s = ar[p+1:n]#.sort()
#         arr = ar[0:p+1]
#         s = s[::-1]
#         for a in s:
#             arr.append(a)
#         print("Next Permutations",arr)
    
def nextPermutation(arr):
    
    n = len(arr)
    p = -1
    for i in range(n-2,-1,-1):
        if arr[i] < arr[i+1]:
            p = i
            break
    
    if p == -1:
        arr.reverse()
        return arr
    for j in range(n-1,p,-1):
        if arr[j] > arr[p]:
            arr[j], arr[p] = arr[p],arr[j]
            break
        
    l,r = p+1,n-1
    
    while l<r:
        arr[l],arr[r] = arr[r],arr[l]
        l += 1
        r -= 1
        
    return arr
    # -----------------------------------------------
    # l = len(arr)
    # t = arr.sort()
    
    # if arr == t:
    #     print(t)
    #     return arr
    
    # else:
        # arr = [2, 4, 1, 7, 5, 0]
        # arr = [1, 2, 3, 6, 5, 4]
        
    # idx1 = 0
    # for i in range(l-2,-1,-1):
    #     if arr[i] < arr[i+1]:
    #         idx1 = i
    #         break
    # p1 = arr[idx1]
    
    # if p1 == arr[0]:
    #     arr1 = arr.sort()
    #     # return arr1
    #     print(arr1)
    #     print(p1)
    
    # else:
    #     idx2 = 0
    #     arr1 = arr[idx1+1:l]
        
    #     p2 = min(arr[idx1+1:l])
    #     for j in range(idx1+1,-1,-1):
    #         p2 = min(arr[idx1+1:l])
            
    #         if arr[j] < p1:
    #             # idx2 = j
    #             del arr[j]
    #         # idx2 = j
    #             # break
    #     idx2 = arr.index(p2)
    #     print("idx2: ",idx2)
    #     print("P2: ",p2) 
        
    #     arr[idx1],arr[idx2] = arr[idx2],arr[idx1]
    #     print(arr)
        
    #     arr1 = arr[idx1+1:l]
    #     arr1 = arr1[::-1]
    #     print("arr1: ",arr1[::-1])
    #     del arr[idx1+1:l]
    #     print("arr: ",arr)
    #     arr.extend(arr1)
    #     print("final: ",arr)
        
            
    
    
if __name__ == "__main__":
    
    # arr = [2, 4, 1, 7, 5, 0]
    # arr = [1, 2, 3, 6, 5, 4]
    # arr = [3,2,1]
    arr = [[2, 4, 1, 7, 5, 0],[3, 2, 1],[3, 4, 2, 5, 1],[1, 2, 3, 6, 5, 4]]
    for a in arr:
        print("Input: ",a)
        print("Next Permutation: ",nextPermutation(a))
             
            
        
    
    
    # t = arr[i+1:l]
    # for j in range(l-1):
    #     if arr[j] > arr[j+1]:
            
            
    
    
    # n = len(arr)
    
    # # Find the pivot index
    # pivot = -1
    # for i in range(n - 2, -1, -1):
    #     if arr[i] < arr[i + 1]:
    #         pivot = i
    #         break
    # print("Pivot Element:",arr[i])
    
    # # If pivot point does not exist, 
    # # reverse the whole array
    # if pivot == -1:
    #     arr.reverse()
    #     return arr

    # # Find the element from the right 
    # # that is greater than pivot
    # for i in range(n - 1, pivot, -1):
    #     if arr[i] > arr[pivot]:
    #         arr[i], arr[pivot] = arr[pivot], arr[i]
    #         break

    # # Reverse the elements from pivot + 1 to the end in place
    # left, right = pivot + 1, n - 1
    # while left < right:
    #     arr[left], arr[right] = arr[right], arr[left]
    #     left += 1
    #     right -= 1

    # return arr


# arr = [2, 4, 1, 7, 5, 0]
# arr = [1, 2, 3, 6, 5, 4]
# arr = [3,2,1]
# print(arr)
# nextPermutation(arr)

# arr = [[2, 4, 1, 7, 5, 0],[3, 2, 1],[3, 4, 2, 5, 1],[1, 2, 3, 6, 5, 4]]

# for a in arr:
#     print("Input: ",a)
#     print(nextPermutation(a))