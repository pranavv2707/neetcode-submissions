class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(not nums):
            return 0
        s=sorted(set(nums))
        maxcount=1
        count=1
        for i in range(1,len(s)):
            if(s[i]-s[i-1]==1):
                count+=1
            else:
                count=1
            print(count)
            maxcount=max(count,maxcount)
        return maxcount
            
        