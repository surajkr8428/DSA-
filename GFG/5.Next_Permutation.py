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
    
    # Find the pivot index
    pivot = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break
    print("Pivot Element:",arr[i])
    
    # If pivot point does not exist, 
    # reverse the whole array
    if pivot == -1:
        arr.reverse()
        return arr

    # Find the element from the right 
    # that is greater than pivot
    for i in range(n - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    # Reverse the elements from pivot + 1 to the end in place
    left, right = pivot + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


arr = [[2, 4, 1, 7, 5, 0],[3, 2, 1],[3, 4, 2, 5, 1],[1, 2, 3, 6, 5, 4]]
for a in arr:
    print("Input: ",a)
    print(nextPermutation(a))