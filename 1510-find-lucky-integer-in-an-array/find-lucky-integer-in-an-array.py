class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dt=Counter(arr)
        ans=[]
        for k,v in dt.items():
            if int(k)==v:
                ans.append(v)
        if ans:
            return max(ans)
        return -1