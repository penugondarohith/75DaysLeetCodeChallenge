class Solution:
    #solution using Hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #creating a Dictionary
        d={}
        #traverse elements through the list 
        for i in range(len(nums)):
            #find number required to Reach the target 
            c=target-nums[i]
            #if c found in dictionary
            if c in d:
                return [d[c],i]
            #else store it with index value 
            d[nums[i]]=i