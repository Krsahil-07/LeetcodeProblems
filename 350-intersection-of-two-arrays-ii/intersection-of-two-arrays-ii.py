class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lib1={}
        for i in range(len(nums1)):
            if nums1[i] in lib1:
                lib1[nums1[i]]+=1
            else:
                lib1[nums1[i]]=1
        lib2={}
        for ii in range(len(nums2)):
            if nums2[ii] in lib2:
                lib2[nums2[ii]]+=1
            else:
                lib2[nums2[ii]]=1
        ans=[]
        for k,v in lib1.items():
            if k in lib2:
                c=min(lib1[k],lib2[k])
                while c:
                    ans.append(k)
                    c-=1
        return ans
