def minChar(s):
    # code here
    
    # f = 0
    # for i in range(1,len(s)):
    #     if s[i] == s[i-1] and s[i] == s[i+1]:
    #         f = i
    #         break
        
    # return len(s) - f - 1
    
    rev = s[::-1]
    temp = s + "#" + rev
    
    lps = [0] * len(temp)
    j = 0
    
    for i in range(1, len(temp)):
        while j > 0 and temp [i] != temp[j]:
            j = lps[j - 1]
            
        if temp[i] == temp[j]:
            j += 1
            
        lps[i] = j
        
    return len(s) - lps[-1]

    
s = "abc"
# s = "aacecaaaa"
print("Input: ",s)
print("Output: ",minChar(s))        