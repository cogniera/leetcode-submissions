#Author Name : Paarth 
#File Name : validPalindrome.py
#Project Name : leetcode-submissions
#Creation Date : 11th September
#Desc : finds if the sentence is a palindrome stripping sentences of any unnecessary content 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1
        
        while left < right:

            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
            
        return True
#Time Complexity: O(n)
#Space Complexity: O(1)
#Time: 7ms Beats 80.78%
#Space: 19.43MB Beats 94.44%
