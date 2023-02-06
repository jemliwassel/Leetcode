class Solution(object):
    def productExceptSelf(self, nums):
        numsLength = len(nums)
        result = [1] * numsLength
        prefix = 1
        for i in range(numsLength) : 
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1 
        for i in range(numsLength-1 , -1 ,- 1):
            result[i] *= postfix
            postfix*= nums[i]   
        return result
