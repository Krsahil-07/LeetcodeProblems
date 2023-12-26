class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y=0,0
        ans=set()
        ans.add((x,y))
        for i in range(len(path)):
            if path[i]=='N':
                y+=1
            if path[i]=='S':
                y-=1
            if path[i]=='E':
                x+=1
            if path[i]=='W':
                x-=1
            if (x,y) in ans:
                return True
            ans.add((x,y))
        return False
        