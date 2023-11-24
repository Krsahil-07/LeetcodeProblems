class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            col=len(nums[i])
            for j in range(col):
                ans.append([i+j,j,nums[i][j]])
        ans.sort()
        lst=[]
        for ele in ans:
            lst.append(ele[2])
        return lst
        