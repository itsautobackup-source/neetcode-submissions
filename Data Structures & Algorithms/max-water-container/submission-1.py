class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i,j = 0, n-1
        max_area = 0
        while i<j:
            h = min(heights[i],heights[j])
            l = j-i
            max_area = max(max_area,l*h)
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
        return max_area