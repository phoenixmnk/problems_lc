# 4
# Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.
#
#
#
# for num
#
# Example 1:
# Input: A = [4,7,9,10], K = 1
# Output: 5
# Explanation:
# The first missing number is 5.
#
# Example 2:
# Input: A = [4,7,9,10], K = 3
# Output: 8
# Explanation:
# The missing numbers are [5,6,8,...], hence the third missing number is 8.
#
# Example 3:
#
# Input: A = [1,3,5], K = 15
# [2,4,6,7,8,9,10,11,12,13,14,15,16,17,18]
#
# Note:
#
# 1 <= A.length <= 50000
# 1 <= A[i] <= 1e7
# 1 <= K <= 1e8

##https://medium.com/@edward.zhou/leet-code-1060-missing-element-in-sorted-array-explained-python3-solution-a1277b6ce32b



class Solution():

    def missing_element(self,nums,k):

        missing_nums=0
        for i in range(1,len(nums)):
            print(nums[i],nums[i-1])
            if nums[i]!=nums[i-1]+1:
                missing_nums+=(nums[i]-nums[i-1])-1

        def missing_search(left, right, newk):
            print(left, right, newk)
            if left == right:
                return None

            if left+1 == right:
                return nums[left]+newk

            middle = (left+right)/2

            totalMissingNum = (nums[middle] - nums[left]) - (middle - left)

            #print totalMissingNum

            if newk > totalMissingNum:
                #print("new",middle, right, newk - totalMissingNum)
                return missing_search(middle, right, newk - totalMissingNum)
            else:
                return missing_search(left, middle, newk)



        if nums[-1]-missing_nums > k:
            return missing_search(0,len(nums)-1,k)
        else:
            return nums[missing_nums]+k-missing_nums


A = [1,3,5]
K = 1
s=Solution()
print(s.missing_element(A,K))



