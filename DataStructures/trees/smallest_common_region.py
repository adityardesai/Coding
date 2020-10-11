"""
You are given some lists of regions where the first region of each list includes all other regions in that list.

Naturally, if a region X contains another region Y then X is bigger than Y. Also by definition a region X contains itself.

Given two regions region1, region2, find out the smallest region that contains both of them.

If you are given regions r1, r2 and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.

It's guaranteed the smallest region exists.

 

Example 1:

Input:
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
Output: "North America"

https://leetcode.com/problems/smallest-common-region/

TC:SC:O(N)
"""
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
        parents_map=dict()
        
        for region in regions:
            parent=region[0]
            children=region[1:]
            for ch in children:
                parents_map[ch]=parent
        
        ancestory_set={region1}
        while region1 in parents_map:
            region1=parents_map[region1]
            ancestory_set.add(region1)
        
        while region2 not in ancestory_set:
            region2=parents_map[region2]
        
        return region2
