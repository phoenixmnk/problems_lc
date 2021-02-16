#2
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#
# Example 1:
# Input: [1,2,3,1]
# Output: true
#
# Example 2:
# Input: [1,2,3,4]
# Output: false
#
# Example 3:
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true


# Method 1

class Solution():

    def method_duplicate1(self,nums):

        return len(nums) == len(set(nums))

nums = [1,2,3]
m=Solution()
print(m.method_duplicate1(nums))



# Method 2

class Solution2():

    def method_duplicate2(self,nums):

        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True

        return False

nums = [1,2,3,1]
m=Solution2()
print(m.method_duplicate2(nums))