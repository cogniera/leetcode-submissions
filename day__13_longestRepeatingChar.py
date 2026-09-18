#Author Name : Paarth Sharma 
#File Name : longestRepeatingChar.py
#Project Name : leetcode-submissions
#Creation Date : 17th September 2026
#Desc : finds the length of the longest substring containing one distict character 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        maxfreq = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxfreq = max(maxfreq, count[s[right]])

            if (right - left + 1) - maxfreq > k:
                count[s[left]] -= 1
                left += 1
            
        return right - left + 1
#Time Complexity : O(n)
#Space Complexity : O(n)
#Time : 54ms Beats 98.89%
#Space : 19.80MB Beats 16.34%
