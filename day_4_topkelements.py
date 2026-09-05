#Author : Paarth Sharma 
#File Name : topkelements.py 
#Project Name : leetcode-submissions 
#Creation Date : 5th September 2026
#Desc : Uses bucket sort to find top k elements in an array 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp = {}

        for item in nums : 
            mp[item] = mp.get(item, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1 )]
    
        for item , freq in mp.items() :

            buckets[freq].append(item)

        output = []

        for freq in range(len(buckets) - 1, 0, -1) :
            
            for item in buckets[freq] : 
                
                output.append(item)

                if len(output) == k:
                    return output
#Time Complexity : O(n) because it operates at max , the lenght of the array given 
#Space Complexity : O(n) 
#Time : 15ms Beats 10.14%
#Memory : 24.95MB Beats 6.32%
