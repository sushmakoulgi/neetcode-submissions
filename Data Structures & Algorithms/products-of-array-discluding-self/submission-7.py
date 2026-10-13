import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_array=[]*len(nums)
        total_product=math.prod(nums)
       
        
        print(total_product)
        for i in range(len(nums)):
            if nums[i]==0:
                new_arr=nums.copy()
                new_arr.remove(nums[i])
                prod_array.append(math.prod(new_arr))
            else:
                prod_array.append(int(total_product/nums[i]))
    

        return prod_array
            
