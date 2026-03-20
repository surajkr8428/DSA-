def maxSubarraySum(nums, k):

    l = len(nums)
    lst = []
    if k == 1:
        return max(nums)
    
    if l % k == 0:
        return sum(nums)

    else:
        for i in range(l):
            for j in range(l):

                l1 = len(nums[i:l-j])
                print(nums[i:l-j])

                if l1 % k == 0 and l1 > 0:
                    print(nums[i:l-j])
                    lst.append(nums[i:l-j])

        lst1 = []
        for a in lst:
            lst1.append(sum(a))
        print("................")
        print("lst",lst)
        print("lst1",lst1)
        return max(lst1)
    
    
# nums = [1,2]; k = 1
# nums = [-1,-2,-3,-4,-5]; k = 4
# nums = [-5,1,2,-3,4]; k = 2
nums = [-10,-1]; k = 1
print(maxSubarraySum(nums, k))