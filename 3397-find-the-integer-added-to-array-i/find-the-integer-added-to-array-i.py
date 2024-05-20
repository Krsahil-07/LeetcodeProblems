class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        a=nums1[0]
        b=nums2[0]
        if a==b:
            return 0
        if a>b:
            return -abs(a-b)
        if a<b:
            return b-a
        