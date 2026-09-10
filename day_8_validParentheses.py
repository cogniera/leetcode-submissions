#Author : Paarth Sharma 
#File Name : validParentheses.py
#Project Name : leetcode-submissions
#Creation Date : 9th september 2026
#Desc : find if, in the given string, every opening bracket has a closing bracket. If yes , then the string is valid 
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        mapping = { ")": "(", "}": "{", "]": "[" }

        isValid = False

        for i in s :
             
            if i in mapping :
                #closing brackets
                expected_open = mapping[i]

                if not stack or stack[-1] != expected_open :
                    return False
                stack.pop()
                        
            else : 
                #opening brackets
                stack.append(i)

        return not stack 
#Time Complexity : O(n)
#Space Complexity : O(n)
#Time : 0ms Beats 44.72%
#Space : 19.24MB Beats 63.19%
