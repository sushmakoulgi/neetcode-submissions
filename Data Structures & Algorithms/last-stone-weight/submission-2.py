class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sorted_stones=sorted(stones)
        while len(sorted_stones) >= 2:
            x=sorted_stones.pop(-1)
            y=sorted_stones.pop(-1)
            sorted_stones.append(abs(x-y))
            sorted_stones=sorted(sorted_stones)
            print(sorted_stones)
       


        return sorted_stones[0]


            