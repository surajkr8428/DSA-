def areRotations(s1,s2):
    # # code here
    
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)
    
    
            
# s1 = "abcd"; s2 = "cdab"
# s1 = "aab"; s2 = "aba"
# s1 = "mightandmagic"; s2 = "andmagicmigth"
s1 = "abcd"; s2 = "acbd"

print("Input: ",s1,s2)
print("Output: ",areRotations(s1, s2))