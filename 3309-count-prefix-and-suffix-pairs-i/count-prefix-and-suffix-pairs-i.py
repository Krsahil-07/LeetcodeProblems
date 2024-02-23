class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt=0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                s=words[i]
                n=len(s)
                if words[i]==words[j][0:n] and words[i]==words[j][-n:]:
                    print(words[j][-n:])
                    print(words[j][0:n])
                    cnt+=1
        return cnt
                
        