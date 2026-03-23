def anagrams(arr):
    '''
    words: list of word
    n:      no of words
    return : list of group of anagram {list will be sorted in driver code (not word in grp)}
    '''

    #code here
    
    d = {}
    
    for i in arr:
        s = ''.join(sorted(i))
        
        if s not in d:
            d[s] = []

        d[s].append(i)
            
    return list(d.values())


# arr = ["act", "god", "cat", "dog", "tac"]
# arr = ["no", "on", "is"]
arr = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]

print("Input: ",arr)
print("Output: ",anagrams(arr))