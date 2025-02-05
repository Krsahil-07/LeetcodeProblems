class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        for i in range(len(l)):
            heavydriver=True
            lst=nums[l[i]:r[i]+1]
            lst.sort()
            print(lst)
            xfactor=lst[1]-lst[0]
            for j in range(len(lst)-1):
                if lst[j+1]-lst[j]!=xfactor:
                    heavydriver=False
                    break
            ans.append(heavydriver)
        return ans
                

        