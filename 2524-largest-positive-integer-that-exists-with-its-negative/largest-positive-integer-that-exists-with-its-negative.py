class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans={}
        for i in range(len(nums)):
            if nums[i]<0:
                if nums[i] in ans:
                    ans[nums[i]]+=1
                else:
                    ans[nums[i]]=1
        mxm=[]
        for ii in range(len(nums)):
            if nums[ii]>0 and -nums[ii] in ans.keys():
                mxm.append(nums[ii])
        print(mxm,ans)
        if len(mxm):
            return max(mxm)
        else:
            return -1
                    

        