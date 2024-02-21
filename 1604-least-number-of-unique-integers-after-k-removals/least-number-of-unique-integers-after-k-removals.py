class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        book=Counter(arr)
        lst=[]
        for key,val in book.items():
            lst.append([val,key])
        lst.sort()
        # print(lst)
        while k:
            a=lst[0]
            if a[0]>k:
                return len(lst)
            if a[0]<=k:
                k-=a[0]
                # print(k)
                lst.pop(0)
        return len(lst)