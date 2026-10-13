from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for s in strs:
            sorteds="".join(sorted(s))

            d[sorteds].append(s)

        res=[]
        for v in d.values():
            res.append(v)

        return res

