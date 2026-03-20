class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = []
        for i in nums:
            if i not in s:
                s.append(i) 
        for i in range(len(s)):
            nums[i] = s[i]
        return len(s)
