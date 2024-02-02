class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=Counter(nums)
        lst=[]
        for k,v in c.items():
            lst.append(v)
        lst.sort(reverse=True)
        ans=lst[0]
        k=lst[0]
        for i in range(1,len(lst)):
            if lst[i]==k:
                ans+=lst[i]
            else:
                break
        return ans


        