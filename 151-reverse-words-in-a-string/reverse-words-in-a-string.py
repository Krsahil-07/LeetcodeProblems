class Solution:
    def reverseWords(self, s: str) -> str:
        ans=s.split()
        i=0
        j=len(ans)-1
        while i<j:
            ans[i],ans[j]=ans[j],ans[i]
            i+=1
            j-=1
        return ' '.join(ans)


        