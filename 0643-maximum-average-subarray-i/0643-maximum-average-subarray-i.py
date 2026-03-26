class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=[]
        i=0
        j=0
        s=0
        while(j<len(nums)):
            if (j-i+1)<k:
                s+=nums[j]
                j+=1
            elif (j-i+1)==k:
                s+=nums[j]
                r=s/float(k)
                l.append(r)
                s-=nums[i]
                i+=1
                j+=1
        return max(l)