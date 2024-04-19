class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # ans=0
        # for i in range(len(nums)):
        #     if nums[i]<k:
        #         ans+=1
        # return ans
        ans=0
        heapify(nums)
        while 1:
            m=heappop(nums)
            if m<k:
                ans+=1
            else:
                break
        return ans