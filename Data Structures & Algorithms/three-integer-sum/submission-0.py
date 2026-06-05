class Solution:
    def two_sum(self, nums1:List[int],k):
        i,j = 0, len(nums1)-1
        pairs= []
        while i<j:
            current_sum = nums1[i]+nums1[j]
            if current_sum == k:
                pairs.append([nums1[i], nums1[j]])
                while i < j and nums1[i] == nums1[i+1]:
                    i += 1
                while i < j and nums1[j] == nums1[j-1]:
                    j -= 1
                i += 1
                j -= 1
            if current_sum > k:
                j -=1
            elif current_sum < k:
                i +=1
        return pairs

        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:  # skip duplicate first elements
                continue
            needed = 0-nums[i]
            two_pair = self.two_sum(nums[i+1:],needed)
            if two_pair:
                print(two_pair,needed, nums[i])
                for pair in two_pair:
                    res.append([nums[i]] + pair)
        return res


        