class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            
            print(r,l)
            print(nums[l:r])
            mid=((r+l)//2)
            print(mid)
            if target==nums[mid]:
                return mid
            if target > nums[mid]:
                l=mid+1
                print(l,r)
                print(nums[l:r])
            else:
                r=mid-1
                print(l,r)
                print(nums[l:r])
            
        return -1
            

        