class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(1,n+1):
            res += i-nums[i-1]
            print(res)
        return res