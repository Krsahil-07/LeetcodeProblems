class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}
        for i in range(len(nums)):
            compl=target-nums[i]
            if compl in ans.keys():
                return [i,ans[compl]]
            else:
                ans[nums[i]]=i
        