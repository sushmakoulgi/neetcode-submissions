from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for num in nums:
            d[num]=d[num]+1
  
        
        sortedArray=sorted(d.values(),reverse=True)
        sortedArray=(sortedArray[:k])
        res=[]
        for key,value in d.items():
            if value in sortedArray:
                res.append(key)
        print(res)
        print(res[:k])
        return res[:k]


      


