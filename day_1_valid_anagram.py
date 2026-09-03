#Author : Paarth Sharma 
#File Name : valid_anagram.py
#Project Name : leetcode-submissions
#Creation Date : 2nd September 2026 
#Description : finds if the two words are a valid anagram of each other 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False 
        
        freq = [0] * 26

        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1

        return all( count == 0 for count in freq) 
#Tests passed : 55/55
#Time : 11ms Beats 77.30%
#Memory : 19.35MB Beats 76.23%
