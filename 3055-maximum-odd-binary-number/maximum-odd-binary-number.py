class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n=len(s)
        c=0
        for i in range(n):
            if s[i]=='1':
                c+=1
        ans=['0']*n
        if c==1:
            ans[-1]='1'
        if c>1:
            ans[-1]='1'
            c-=1
            j=0
            while c:
                ans[j]='1'
                j+=1
                c-=1
        return "".join(ans)
        
        
        