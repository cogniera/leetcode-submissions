#Author : Paarth Sharma
#File Name : groupAnagrams.py
#Project Name : leetcode-submissions
#Creation date: 4th september 2026
#Desc : finds anagrams in a list and then creates a list of lists with all the anagrams grouped together 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        store = {}

        for word in strs:

            freq = [0] * 26
            for l in word : 
                freq[ord(l) - ord('a')] += 1
            
            key = tuple(freq)
            
            if key not in store : 
                store[key] = []
            
            store[key].append(word)

        output = []

        for i in store : 

            output.append(store[i])
        
        return output
# Time Complexity : O(n*k) where k is the length of the word , n is the number of words in the given list 
# Space Complexity : O(S) where s is roughly n * k given that k is the size of the words and all the words have roughly the same amount of characters  
# Time: 16ms Beats 27.02%
# Memory : 24.12MB Beats 9.62%
