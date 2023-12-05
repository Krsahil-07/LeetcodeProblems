class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=[]
        for i in range(len(num)-2):
            s=num[i:i+3]
            # print(s)
            if s[0]==s[1] and s[1]==s[2]:
                # print(type(s))
                ans.append(int(s))
        # print(ans)
        if ans:
            a=max(ans)
            if a==0:
                a='000'
            return str(a)
        else:
            return ''



       