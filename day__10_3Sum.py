#Author : Paarth Sharma 
#File name : 3Sum.py
#Project Name : leetcode-submissions
#Creation Date : 
#Desc : finds groups of ints , whose sums are 0 
class Solution : 
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
      nums.sort()
        
        output = []
        
        for idx in range(len(nums) - 2):
            
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            
            left ,right = idx+1, len(nums) - 1

            while left < right:
                
                sum = nums[idx] + nums[left] + nums[right]
                
                if sum < 0:
                    left += 1
                
                elif sum > 0:
                    right -= 1
                
                else : 
                    
                    output.append([nums[idx], nums[left], nums[right]])
                    
                    left += 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        
        return output
#Time Complexity : O(n^2)
#Space Complexity : O(n) 
#Time : 627ms Beats 60.95%
#Space : 22.14MB Beats 82.32%
