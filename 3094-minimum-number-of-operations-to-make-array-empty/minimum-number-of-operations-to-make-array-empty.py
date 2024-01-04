class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d=Counter(nums)

        ans=0
        for i in d:
            ans+=math.ceil(d[i]/3)
            if d[i]==1:
                return -1
        print(d)
        return ans

        