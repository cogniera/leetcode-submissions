#Author : Paarth Sharma 
#File Name : productOfArray.py
#Project Name : leetcode-submissions
#Creation Date : 7th September 2026
#Desc : makes an output array where the output is a product of every element in the array except the element itself making use of the suffix and prefix strategy 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1] * len(nums)

        prefix = 1
        for i in range(1, len(nums) + 1) :
            output[i-1] *= prefix 
            prefix *= nums[i-1]

        suffix = 1
        for i in range(len(nums), 0, -1):
            output[i-1] *= suffix
            suffix *= nums[i-1]
        
        return output
#Time Complexity : O(n) as 2 N iteration loops 
#Space Complexity : O(n) if the output array is included , and O(1) if it is excluded 
#Time : 110ms Beats 60.71%
#Space : 10.0 MB Beats 50.68%
