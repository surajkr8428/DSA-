def search(pat, txt):
    # code here
    
    n = len(pat)
    l = []
    
    for i in range(len(txt)):
        if pat == txt[i:i+n]:
            l.append(i)
            print(txt[i:i+n+1])
    return l
            

# txt = "abesdu"; pat = "edu"
txt = "aabaacaadaabaaba"; pat = "aaba"
# txt = "abcab"; pat = "ab"
print(search(pat, txt))
    
        