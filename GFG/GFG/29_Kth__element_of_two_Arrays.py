def kthElement(a, b, k):
    # code here

    a.extend(b)
    a.sort()

    return a[k-1]


a = [2, 3, 6, 7, 9]; b = [1, 4, 8, 10]; k = 5
a = [1, 4, 8, 10, 12]; b = [5, 7, 11, 15, 17]; k = 6

print("Input: ",a,b,k)
print("Output: ",kthElement(a, b, k))