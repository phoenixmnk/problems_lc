#3
#  Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

class Solution():

    def combination_sum(self,candidates,target):

        Solution.res=[]


        self.dfs(candidates,target,0,[])
        #print("iteration")
        return Solution.res


    def dfs(self,candidates,target,start,Values):

        l= len(candidates)
        if target ==0:
            return Solution.res.append(Values)

        #print Values,start,l
        for i in range(start,l):
            print(i,candidates[i],target)
            if candidates[i] > target:
                return
            print("iteration1", candidates, target-candidates[i],i,Values+[candidates[i]])
            self.dfs(candidates,target-candidates[i],i,Values+[candidates[i]])

candidates = [2,3,5]
target = 8

s=Solution()
print(s.combination_sum(candidates,target))