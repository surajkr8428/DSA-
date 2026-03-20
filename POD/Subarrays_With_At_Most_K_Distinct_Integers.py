
# def countAtMostK(arr,k):
    # Code here

arr = [1, 2, 2, 3]
k = 2
l = len(arr)
a = []
print(arr)
for i in range(l):
    for j in range(i+1):
        if len(arr[j:i+j]) > 0:
            a.append(arr[j:i+j])
                
    # return a
print(a)


# print(countAtMostK(arr,k))

