#1
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution():

    def two_sum(self,nums,target):
        d={}

        for idx,num in enumerate(nums):
            diff = target-num
            if diff in d:
                return [d[diff], idx]
            else:
                d[num] = idx
                

nums = [2, 11, 7, 15]
target = 9


res=Solution()
print(res.two_sum(nums,target))
