class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        cnt=0
        for i in range(len(nums)):
            if nums[i]&1:
                continue
            else:
                cnt+=1
        if cnt>=2:
            return True
        else:
            return False
        