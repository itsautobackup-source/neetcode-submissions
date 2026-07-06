class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_mx,right_mx,res = [0]*n,[0]*n,0
        left_mx[0] = height[0]
        right_mx[n-1]= height[n-1]
        for i in range(1,n):
            left_mx[i] = max(height[i],left_mx[i-1])
        for j in range(n-2,-1,-1):
            right_mx[j] = max(height[j],right_mx[j+1])
        for i in range(n):
            val = min(right_mx[i],left_mx[i]) - height[i]
            res+= val if val>0 else 0
        return res
        
