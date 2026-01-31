def hIndex(self, citations):
    #code here
    
    citations.sort(reverse = True)
    n = len(citations)
    
    i = 0
    while i < n and citations[i] > i:
        i += 1
    
    return i


citations = [[3, 0, 5, 3, 0],[5, 1, 2, 4, 1],[0, 0]]
for c in citations:
    print("Input: ",c)
    print("Output: ",hIndex(0, c))