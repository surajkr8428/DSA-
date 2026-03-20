def maxSubarraySum(nums, k):
    
    if not nums:
        return 0

    else:
        m_sum = 0
        
        for i in range(k):
            m_sum += nums[i]
        c_sum = m_sum   
        for i in range(k, len(nums)):
            c_sum += nums[i] - nums[i-k]
            m_sum = max(m_sum, c_sum)   
        return m_sum
    
    
    
    
    
    
nums = [1,2]; k = 1
print("Input: ",nums,k)
print("Output: ",maxSubarraySum(nums, k))