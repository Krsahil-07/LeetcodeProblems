class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1={}
        h2={}
        for i in range(len(s)):
            if s[i] in h1:
                h1[s[i]]+=1
            else:
                h1[s[i]]=1
        for ii in range(len(t)):
            if t[ii] in h2:
                h2[t[ii]]+=1
            else:
                h2[t[ii]]=1
        if h1==h2:
            return True
        else:
            return False
        