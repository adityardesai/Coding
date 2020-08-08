class Solution:
    def brute_force(self, heights):
        """
        TC:O(n^2) TLE
        SC:O(1)
        """
        n=len(heights)
        max_area=0
        
        for i in range(n):
            min_height=float('inf')
            for j in range(i,n):
                min_height=min(min_height, heights[j])
                max_area=max(max_area, min_height * (j-i+1))
        return max_area
    def divide_and_conquer_helper(self,heights, start, end):
        """
        TC:O(nlogn) TLE
        SC:O(n)
        """
        if start>end:
            return 0
        
        min_index=start
        for i in range(start, end+1):
            if heights[min_index]>heights[i]:
                min_index=i
            
            res1=heights[min_index]*(end-start+1)
            res2=self.divide_and_conquer_helper(heights,start,min_index-1)
            res3=self.divide_and_conquer_helper(heights,min_index+1,end)
            
            max_area=max(res1, max(res2, res3))
            
        return max_area
        
    def divide_and_conquer(self, heights):
        return self.divide_and_conquer_helper(heights, start=0, end=len(heights)-1)
    def stack_helper(self, heights):
        """
        TC: O(N)
        SC: O(N)
        """
        n=len(heights)
        stack=list()
        max_area=0
        stack.append(-1)
        
        for i in range(n):
            while (stack[-1]!=-1 and heights[i]<=heights[stack[-1]]):
                temp_area=heights[stack.pop()] * (i-stack[-1]-1)
                max_area=max(max_area,temp_area)
            stack.append(i)
        
        while stack[-1]!=-1:
            max_area=max(max_area, heights[stack.pop()] * (n-stack[-1]-1))
        
        return max_area
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights or len(heights)==0:
            return 0
        #return self.brute_force(heights)
        #return self.divide_and_conquer(heights)
        return self.stack_helper(heights)