def aggressive_cows(stalls, k):
    # Sort the stall positions
    stalls.sort()
    
    # Helper function to check if cows can be placed
    def can_place(min_dist):
        count = 1  # First cow in first stall
        last_position = stalls[0]
        
        for i in range(1, len(stalls)):
            if stalls[i] - last_position >= min_dist:
                count += 1
                last_position = stalls[i]
                
                if count == k:
                    return True
        return False
    
    # Binary search for the answer
    low = 1
    high = stalls[-1] - stalls[0]
    answer = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        if can_place(mid):
            answer = mid
            low = mid + 1  # Try for a bigger minimum distance
        else:
            high = mid - 1  # Reduce distance
    
    return answer


# Example usage
print(aggressive_cows([1, 2, 4, 8, 9], 3))       # Output: 3
print(aggressive_cows([10, 1, 2, 7, 5], 3))      # Output: 4
print(aggressive_cows([2, 12, 11, 3, 26, 7], 5)) # Output: 1