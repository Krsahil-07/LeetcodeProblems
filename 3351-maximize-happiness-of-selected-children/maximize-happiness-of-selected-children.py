class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans=0
        decay=0
        i=0
        while k:
            if (happiness[i]-decay)>0:
                ans+=happiness[i]-decay
                k-=1
                i+=1
                decay+=1
            else:
                ans+=0
                i+=1
                k-=1
        return ans




        