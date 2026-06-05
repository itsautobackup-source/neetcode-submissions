class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        # for s in strs:
        #     k = ''.join(sorted(s))
        #     if k not in d:
        #         d[k] = []
        #     d[k].append(s)
        # return list(d.values())
        for s in strs:
            cnt = [0]*26
            for c in s:
                key = ord(c)-ord('a')
                cnt[key] +=1
            if tuple(cnt) not in d:
                d[tuple(cnt)] = []
            d[tuple(cnt)].append(s)
        return list(d.values())

