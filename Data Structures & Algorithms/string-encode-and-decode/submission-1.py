class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append('#')
            encoded.append(s)
        return ''.join(encoded)


    def decode(self, s: str) -> List[str]:
        i=0
        res = []
        while i<len(s):
            l = ''
            while s[i]!='#':
                l +=s[i]
                i+=1
            i+=1 # to exclude #
            res.append(s[i:int(l)+i])
            i += int(l)
        return res

        
