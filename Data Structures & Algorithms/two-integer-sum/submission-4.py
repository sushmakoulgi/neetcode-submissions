class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            first=nums[i]
            secondnumber=target-first
            if secondnumber in nums:
                for j in range(i+1,len(nums)):
                   if nums[j]==secondnumber:
                    return [i,j]
        return []
        