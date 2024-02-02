class Solution:
    def countKeyChanges(self, s: str) -> int:
        s=s.upper()
        cnt=0
        k=s[0]
        for i in range(1,len(s)):
            if s[i]==k:
                continue
            else:
                k=s[i]
                cnt+=1
        return cnt
        