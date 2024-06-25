class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            if nums[i]%3!=0:
                c+=min(abs(nums[i]%3-3),abs(nums[i]%3-0))
        return c
        