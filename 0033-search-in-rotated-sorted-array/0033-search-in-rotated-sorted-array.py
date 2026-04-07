class Solution(object):
    def search(self, nums, target):
        val=-1
        for i in range(len(nums)):
            if target==nums[i]:
                val=i
                break
        return val