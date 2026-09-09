#Author : Paarth Sharma 
#File Name : longestConsecSeq.py
#Project Name : leetcode-submissions
#Creation Date : 8th September 2026
#Desc : find the number of the longest Consecutive sequence in the given array , there is no ordering required for the sequence i.e. 2,3,4 is a seq and 4,3,2 is also a seq and so is 2,4,3 thus it is a set 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_streak = 0

        for num in num_set : 

            if num-1 not in num_set : 
                current_num = num
                current_streak = 1

                while (current_num + 1) in num_set : 
                    current_num += 1
                    current_streak += 1
                
                if current_streak > max_streak : 

                    max_streak = current_streak
        
        return max_streak
#Time Complexity : O(n)  
#Space Complexity : O(n)
#Time : 51ms Beats 53.73%
#Space : 36.56MB Beats 66.75%
