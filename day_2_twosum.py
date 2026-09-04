#Author : Paarth Sharma 
#File Name : twosum.py
#Project Name : leetcode-submissions
#Creation Date : 3rd September 2026
#Desc : find if there are two elements in the array that sum to a given target 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, num in enumerate(nums):
            complement = target - num 

            if complement in mp : 
                return [mp[complement], i]
            
            mp[num] = i
        
        return []
#Test Cases Passed : 65/65
#Time : 3ms Beats 53.59%
#Memory : 20.50MB Beats 41.70%
