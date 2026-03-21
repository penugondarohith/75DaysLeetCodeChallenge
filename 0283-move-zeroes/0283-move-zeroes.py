class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c=0
        for i in range(len(nums)):
            if nums[i]==0:
                c+=1
        for i in range(c):
            nums.remove(0)
        n=[0]*c
        nums.extend(n)
        return nums