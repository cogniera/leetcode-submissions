#Author : Paarth Sharma  
#FileName : encodedecode.py
#ProjectName : leetcode-submissions
#Creation Date: 6th september 2026
#Desc : encode and decode strings as two seperate functions 
class Solution:

    def encode(self, strs: List[str]) -> str:
        
        string = ""
        
        for word in strs:
        
            string += f"{len(word)}-{word}"
        
        return string

    def decode(self, s: str) -> List[str]:
        
        output = []

        i = 0
        
        while i < len(s):
            
            idx = s.find('-', i)
            
            length = int(s[i:idx])
            
            output.append(s[idx + 1 : idx + 1 + length])
            
            i = idx + 1 + length

        return output
#Time Complexity : O(n) for encode , O(n) for decode 
#Space Complexity : O(n) for encode , O(n) for decode 
#Time : 28ms Beats 99.90%
#Space : 8.3 MB Beats 7.86%
