class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen=set()
        for item in nums:
            if item in seen:
                return item
            seen.add(item)

        return None
