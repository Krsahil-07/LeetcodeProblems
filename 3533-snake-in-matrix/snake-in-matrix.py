class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        ans=[]
        l=0
        for i in range(n):
            c=[]
            for j in range(n):
                c.append(l)
                l+=1
            ans.append(c)
        # print(ans)
        ii=0
        jj=0
        for ele in commands:
            if ele=="DOWN":
                ii+=1
            if ele=="UP":
                ii-=1
            if ele=="RIGHT":
                jj+=1
            if ele=="LEFT":
                jj-=1
        return ans[ii][jj]

        