from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        
        zero_count = nums.count(0)
        
        # Calculate product of non-zero elements
        p = 1
        for num in nums:
            if num != 0:
                p *= num
        
        for i in range(len(nums)):
            if zero_count > 1:
                res.append(0)
            elif zero_count == 1:
                if nums[i] == 0:
                    res.append(p)
                else:
                    res.append(0)
            else:
                res.append(p // nums[i])
        
        return res