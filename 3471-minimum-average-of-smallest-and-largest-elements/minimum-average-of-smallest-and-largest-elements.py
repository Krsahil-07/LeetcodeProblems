class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        ans=float('inf')
        i=0
        j=len(nums)-1
        while i<j:
            a=(nums[i]+nums[j])/2
            ans=min(ans,a)
            i+=1
            j-=1
        return ans
        