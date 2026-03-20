def twoSum(self, arr, target):
	# code here
	
	arr.sort()
	
	l,r = 0,len(arr)-1
	
	while l<r:
		s = arr[l] + arr[r]
		
		if s == target:
			return True
		
		elif s < target:
			l += 1
			
		else:
			r -= 1
		
	return False


arr = [0, -1, 2, -3, 1]; target = -2
# arr = [1, -2, 1, 0, 5]; target = 0
# arr = [11]; target = 11

print("Input: ",arr,target)
print("Output: ",twoSum(None, arr, target))
