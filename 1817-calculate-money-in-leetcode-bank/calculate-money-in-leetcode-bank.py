class Solution:
    def totalMoney(self, n: int) -> int:
        ans=[]
        initial_week_val=28
        c_week=n//7
        e_days=n-(c_week*7)
        for i in range(c_week):
            ans.append(initial_week_val)
            initial_week_val+=7
        # print(ans)
        summ=0
        for ii in range(1,e_days+1):
            summ+=c_week+ii
            # print(summ)
        ans.append(summ)
        # print(ans)
        return sum(ans)


            
        