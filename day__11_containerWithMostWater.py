#Author : Paarth Sharma 
#File Name : containerWithMostWater.py
#Project Name : leetcode-submissions
#Creation Date : 15th september 2026
#Desc : find the container in the array with most area 
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left , right = 0 , len(heights) - 1

        output = 0

        while left < right : 
            area = min(heights[left], heights[right]) * (right - left)
            output = max(output, area)

            if heights[left] < heights[right] : 
                left += 1
            else : 
                right -= 1

        return output
#Time Complexity : O(n) 
#Space Complexity : O(1)
#Time : 63ms Beats 25.65%
#Space : 29.61MB Beats 38.80%
