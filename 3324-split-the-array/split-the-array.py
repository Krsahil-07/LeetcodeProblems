class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        ans={}
        for i in range(len(nums)):
            if nums[i] not  in ans:
                ans[nums[i]]=1
            else:
                ans[nums[i]]+=1
        print(ans)
        for k,val in ans.items():
            if val>2:
                return False
        return True
        