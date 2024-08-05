class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans={}
        for ele in arr:
            if ele not in ans:
                ans[ele]=1
            else:
                ans[ele]+=1
        lst=[]
        for key,val in ans.items():
            if val==1:
                a=key
                b=arr.index(key)
                lst.append([b,a])
        lst.sort()
        if len(lst)<k:
            return ''
        else:
            hehehe=lst[k-1]
            return hehehe[1]

        
        