from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist=Counter(s)
        tlist=Counter(t)
        for key,count in slist.items():
            if key not in tlist or count !=tlist[key]:
                return False
            else:
                del tlist[key]
        if len(tlist) > 0:
            return False
       
        return True