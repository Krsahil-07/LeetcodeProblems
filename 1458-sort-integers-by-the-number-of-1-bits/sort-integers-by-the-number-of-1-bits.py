class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ans=[]
        for i in range(len(arr)):
            n=(bin(arr[i])[2:]).count('1')
            ans.append([n,arr[i]])
        ans.sort()
        lst=[]
        for j in range(len(ans)):
            lst.append(ans[j][1])
        return lst
        