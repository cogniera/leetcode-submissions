#Author Name : Paarth Sharma
#File Name : longestSubstringWithoutDuplicate.py
#Project Name : leetcode-submissions
#Creation Date : 16th September 2026
#Desc : finds the longest substring that has unique characters 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        seen = set()

        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            length = max(length, R - L + 1)
            
        return length
#Time Complexity : O(n)
#Space Complexity : O(k) where k is the set of characters used
#Time : 181ms Beats 71.38%
#Space : 19.91MB Beats 30.15%
