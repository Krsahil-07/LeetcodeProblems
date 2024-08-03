class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        s=list(s)
        ans=''
        for i in range(len(s)):
            ans+=s[(i+k)%len(s)]
        return ans
        