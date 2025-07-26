class Solution:
    def possibleStringCount(self, word: str) -> int:
        cnt=1
        c_char=word[0]
        for i in range(1,len(word)):
            if c_char==word[i]:
                cnt+=1
            else:
                c_char=word[i]
        return cnt

        