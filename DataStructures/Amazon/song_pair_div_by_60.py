"""
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/submissions/

Platform: HackerRank
Position: Experienced

Amazon Music Pairs

Amazon Music is working on a new "community radio station" feature which will allow users to iteratively populate
the playlist with their desired songs. Considering this radio station will also have other scheduled shows to be
aired, and to make sure the community soundtrack will not run over other scheduled shows, the user-submitted songs
will be organized in full-minute blocks. Users can choose any songs they want to add to the community list, but
only in pairs of songs with durations that add up to a multiple of 60 seconds (e.g. 60, 120, 180).

As an attempt to insist on the highest standards and avoid this additional burden on users, Amazon will let them
submit any number of songs they want, with any duration, and will handle this 60-second matching internally. Once
the user submits their list, given a list of song durations, calculate the total number of distinct song pairs that
can be chosen by Amazon Music.

Example

n = 3

songs = [37, 23, 60]
One pair of songs can be chosen whose combined duration is a multiple of a whole minute (37 + 23 = 60) and the
return value would be 1. While the third song is a single minute long, songs must be chosen in pairs.
"""

class Solution:
    def numPairsDivisibleByK(self, time,k):
        hash_map=dict()
        count=0
        for i in range(len(time)):
            a=time[i]
            b=(k-a)%k
            count=count + hash_map.get(b,0)
            hash_map[a%k]=1+hash_map.get(a%k,0)
            print(hash_map)
        return count
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if not time:
            return
        return self.numPairsDivisibleByK(time,60)
