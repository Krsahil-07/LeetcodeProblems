class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(1,numRows+1):
            if i==1:
                ans.append([1])
            if i==2:
                ans.append([1,1])
            if i>2:
                lst=[]
                lst.append(1)
                a=ans[-1]
                for j in range(len(a)-1):
                    lst.append(a[j]+a[j+1])
                lst.append(1)
                ans.append(lst)
                lst=[]
        return ans


        