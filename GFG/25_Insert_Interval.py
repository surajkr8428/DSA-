def insertInterval(self, intervals, newInterval):
    # Code here
    
    result = []
    i = 0
    n = len(intervals)
    
    n_s, n_e = newInterval
    
    while i < n and intervals[i][1] <n_s:
        result.append(intervals[i])
        i += 1
        
    while i < n and intervals[i][0] <= n_e:
        n_s = min(n_s,intervals[i][0])
        n_e = max(n_e,intervals[i][1])
        i += 1
        
    result.append([n_s,n_e])
    
    while i < n:
        result.append(intervals[i])
        i += 1
        
    return result


# intervals = [[1, 3], [4, 5], [6, 7], [8, 10]]; newInterval[] = [5, 6]
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]; newInterval = [4, 9]

print("Input: ",intervals,newInterval)
print("Output: ",insertInterval(0, intervals, newInterval))