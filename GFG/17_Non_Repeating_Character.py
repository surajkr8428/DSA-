def nonRepeatingChar(s):
    #code here
    
    d = {}
    d_k = []
    d_v = []
    
    for i in s:
        if i not in d_k:
            d[i] = s.count(i)
            d_k.append(i)
            # d_v.append(d[i])
            if d[i] == 1:
                return i
    
    return "$"



s = ["geeksforgeeks","racecar","aabbccc""aabbccc"]
for i in s:
    print("Input: ",i)
    print("Output: ",nonRepeatingChar(i))