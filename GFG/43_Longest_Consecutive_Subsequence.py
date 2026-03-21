def longestConsecutive(arr):
    
    n_s = set(arr)
    m_l = 0
    
    if not arr:
        return 0
    
    for n in arr:
        if n - 1 in n_s:
            continue
        
        c_l = 1
        nxt_n = n + 1
        
        while nxt_n in n_s:
            c_l += 1
            nxt_n += 1
            
        m_l = max(m_l, c_l)
    
    return m_l


arr = [2, 6, 1, 9, 4, 5, 3]
# arr = [1, 9, 3, 10, 4, 20, 2]
# arr = [15, 13, 12, 14, 11, 10, 9]

print("Input: ",arr)
print("Output: ",longestConsecutive(arr))
        