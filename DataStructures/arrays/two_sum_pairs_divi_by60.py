# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# TC: O(N)
# SC: O(1)
class Solution:
    def numPairsDivisibleByK(self, time,k):
        hash_map=dict()
        count=0
        for i in range(len(time)):
            a=time[i]
            b=(k-a%k)%k
            count=count + hash_map.get(b,0)
            hash_map[a%k]=1+hash_map.get(a%k,0)
        return count
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if not time:
            return
        return self.numPairsDivisibleByK(time,60)
