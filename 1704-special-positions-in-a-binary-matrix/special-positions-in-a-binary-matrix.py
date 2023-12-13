class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r=len(mat)
        c=len(mat[0])
        ans=0
        for i in range(r):
            for j in range(c):
                if mat[i][j]==0:
                    continue
                re=0
                ce=0
                for ii in range(r):
                    if mat[ii][j]==1:
                        re+=1
                for jj in range(c):
                    if mat[i][jj]==1:
                        ce+=1
                if re==1 and ce==1:
                    ans+=1
        return ans


        