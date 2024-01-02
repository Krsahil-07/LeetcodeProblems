class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        map={}
        ans=[]
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]]=1
            else:
                map[nums[i]]+=1
        while map:
            temp=[]
            del_ele=[]
            for k,v in map.items():
                temp.append(k)
                v-=1
                if v==0:
                    del_ele.append(k)
                map[k]=v
            ans.append(temp)
            for i in del_ele:
                del map[i]
        return ans
        