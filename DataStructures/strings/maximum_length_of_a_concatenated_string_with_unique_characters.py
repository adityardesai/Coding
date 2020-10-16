class Solution:
    max_len=float('-inf')
    def brute_force_helper(self, arr):
        """
        Does not work for all cases
        """
        n=len(arr)
        max_length=float('-inf')
        for i in range(n):
            m_set=set(arr[i])
            for j in range(i+1, n):
                n_set=set(arr[j])
                if not m_set.intersection(n_set):
                    max_length=max(max_length, len(m_set) + len(n_set))
        return max_length
    
    def duplicates(self, s):
        if len(s) != len(set(s)):
            return True
        return False
    
    def backtrack_helper(self, arr, solution_so_far,start_index):
        self.max_len=max(self.max_len, len(solution_so_far))
        if start_index == len(arr):        
            return
        for i in range(start_index, len(arr)):    
            if not self.duplicates(solution_so_far + arr[i]):
                self.backtrack_helper(arr, solution_so_far+arr[i], i+1)

    def maxLength(self, arr: List[str]) -> int:
        if not arr:
            return 0
        #return self.brute_force_helper(arr)        
        start_index=0
        self.backtrack_helper(arr, '', start_index)
        return self.max_len

        
