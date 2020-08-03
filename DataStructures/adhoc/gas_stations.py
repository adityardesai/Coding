# https://leetcode.com/problems/gas-station/
# TC:O(N)
# SC:O(1)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        gas  = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        """
        total_gas=0
        curr_gas=0
        N=len(gas)
        starting_pt=0
        
        for i in range(N):
            
            total_gas=total_gas+gas[i]-cost[i]
            curr_gas=curr_gas+gas[i]-cost[i]
            
            if curr_gas<0:
                curr_gas=0
                starting_pt=i+1
        
        if total_gas>=0:
            return starting_pt
        else:
            return -1