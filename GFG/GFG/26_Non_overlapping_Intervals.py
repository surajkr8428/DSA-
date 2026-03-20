
def minRemoval(intervals):
    # code here
    
    if not intervals:
        return 0
        
    intervals.sort(key = lambda x: x[1])
    
    removals = 0
    p_end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < p_end:
            removals += 1
            
        else:
            p_end = intervals[i][1]
    
    return removals


intervals = [[[1, 2], [2, 3], [3, 4], [1, 3]],[[1, 3], [1, 3], [1, 3]],[[1, 2], [5, 10], [18, 35], [40, 45]]]
for i in intervals:
    print("Input: ",i)
    print("Output: ",minRemoval(i))