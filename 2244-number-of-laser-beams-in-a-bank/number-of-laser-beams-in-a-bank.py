class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lst=[]
        for i in range(len(bank)):
            a=bank[i].count('1')
            if a:
                lst.append(a)
        # print(lst)
        ans=0
        for i in range(len(lst)-1):
            ans+=(lst[i]*lst[i+1])
        return ans
        