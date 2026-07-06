class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        i=0
        d = {}
        for j in range(len(s)):
            d[s[j]] = d.get(s[j],0)+1
            while d[s[j]]>1:
                d[s[i]]-=1
                i+=1
            max_l = max(max_l,j-i+1)
        return max_l
