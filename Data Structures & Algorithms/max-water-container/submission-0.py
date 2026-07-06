class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0,len(heights)-1
        max_area = 0
        while i<j:
            left = heights[i]
            right = heights[j]
            h = min(left,right)
            l = j-i
            max_area = max(max_area,l*h)
            if left<=right:
                i+=1
            else:
                j-=1
        return max_area