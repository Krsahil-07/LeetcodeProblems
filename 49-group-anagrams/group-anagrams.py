class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        lst=[]
        for ele in strs:
            new="".join(sorted(ele))
            if new in ans:
                ans[new].append(ele)
            else:
                ans[new]=[ele]
        for k,v in ans.items():
            lst.append(v)
        return lst

        