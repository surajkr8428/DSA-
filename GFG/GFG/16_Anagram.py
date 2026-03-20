def areAnagrams(s1, s2):
       # code here
       
       
        if len(s1) != len(s2):
            return False
        
        freq = {}
        
        for i in s1:
            freq[i] = freq.get(i,0) + 1
            
        for j in s2:
            if j not in freq:
                return False
                
            freq[j] -= 1
            
            if freq[j] < 0:
                return False
                
        return True
    
    
s = {'s1': "geeks", 's2': "kseeg", 's3': "allergy", 's4': "allergyy",'s5': "listen", 's6': "lists"}

print(areAnagrams(s.get('s1'),s.get('s2')))