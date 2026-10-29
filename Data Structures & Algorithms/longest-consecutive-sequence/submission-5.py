class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        print(nums)
        max_count=0
        count=0
        for i in range(len(nums)):
            if i==0:
                count+=1
            elif nums[i]-1==nums[i-1] :
                count+=1
            elif nums[i]==nums[i-1]:
                pass
            else:
                max_count=max(max_count,count)
                count=1

        max_count=max(max_count,count)
        return max_count