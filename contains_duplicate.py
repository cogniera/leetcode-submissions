#Author : Paarth Sharma 
#File Name : contains_duplicate.py 
#Project Name : leetcode-submissions 
#Creation Date : 2nd September 2026 
#Desc : find if there is duplicate in an array 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums : 
            if num in seen : 
                return True 
            else : 
                seen.add(num)
        return False 
#Test Cases Passed : 79  
#Time : 11ms Beats 82.44%
#Memory : 32.22 MB Beats 54.60%
