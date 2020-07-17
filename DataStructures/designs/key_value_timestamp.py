# https://leetcode.com/problems/time-based-key-value-store/
# TC: O(1) for set O(logN) for get
# SC: O(N)
class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((value, timestamp))

    def helper_binary_search(self, arr, target):
        N = len(arr)
        low = 0
        high = N - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid][1] == target:
                return mid
            elif arr[mid][1] < target:
                low = mid + 1
            else:
                high = mid - 1
        return high

    def get_binary_search(self, key, timestamp):
        """
        Since timestamp is monotonically increasing, 
        it is sorted so we can use the binary search.
        """
        if not self.hash_map[key]:
            return ''
        else:
            arr = self.hash_map[key]
            index = self.helper_binary_search(arr=arr, target=timestamp)
            if arr[index][1] <= timestamp:
                return arr[index][0]
            else:
                return ''

    def get(self, key: str, timestamp: int) -> str:
        return self.get_binary_search(key, timestamp)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
