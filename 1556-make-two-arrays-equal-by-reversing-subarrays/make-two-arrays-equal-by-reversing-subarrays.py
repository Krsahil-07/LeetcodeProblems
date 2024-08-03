class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        ans={}
        ans1={}
        for ele in target:
            if ele not in ans:
                ans[ele]=1
            else:
                ans[ele]+=1
        for c in arr:
            if c not in ans1:
                ans1[c]=1
            else:
                ans1[c]+=1
        if ans==ans1:
            return True
        else:
            return False
        