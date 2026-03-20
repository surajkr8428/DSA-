def areRotations(s1,s2):
    # # code here
    # n1 = len(s1)
    # n2 = len(s2)
        
    # if s1 == s2:
    #     return True
    
    # else:
        
    #     i = 0
        
    #     while s1 != s2:
            
    #         t = s1[0]
    #         s1 = s1[1:n1] + s1[0]       # t[::-1]
    #         print(s1)
            
    #         if i == n1 or s1 == s2:
    #             break
    #         i += 1
            
            
    #     return s1 == s2
    
# def areRotations(s1, s2):
    # n = len(s1)

    # # generate and check all possible rotations of s1
    # for _ in range(n):
        
    #     # if current rotation is equal to s2 return true
    #     if s1 == s2:
    #         return True

    #     # Right rotate s1
    #     s1 = s1[-1] + s1[:-1]

    # return False
    
    
    n = len(pat)
    lps = [0] * n
  
    # length of the previous longest prefix suffix
    patLen = 0

    # lps[0] is always 0
    lps[0] = 0

    # loop calculates lps[i] for i = 1 to n-1
    i = 1
    while i < n:
      
        # if the characters match, increment len 
        # and extend the matching prefix
        if pat[i] == pat[patLen]:
            patLen += 1
            lps[i] = patLen
            i += 1
      
        # If there is a mismatch
        else:
          
            # If len is not zero, update len to
            # last known prefix length
            if patLen != 0:
                patLen = lps[patLen - 1]
            # No prefix matches, set lps[i] = 0
            # and move to the next character
            else:
                lps[i] = 0
                i += 1
    return lps
            
# s1 = "abcd"; s2 = "cdab"
# s1 = "aab"; s2 = "aba"
s1 = "abcd"; s2 = "acbd"

print("Input: ",s1,s2)
print("Output: ",areRotations(s1, s2))