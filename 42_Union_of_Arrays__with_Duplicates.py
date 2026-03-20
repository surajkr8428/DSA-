def findUnion(a, b):
    # code here
    a.extend(b)
    a = set(a)
    return a


a = [1, 2, 3, 2, 1]; b = [3, 2, 2, 3, 3, 2]
# a = [1, 2, 3]; b = [4, 5, 6]
# a = [1, 2, 1, 1, 2]; b = [2, 2, 1, 2, 1] 

print("Input: ",a,b)
print("Output: ",findUnion(a, b))