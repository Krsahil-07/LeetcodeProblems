class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt=0
        for i in range(len(details)):
            a=details[i][11:13]
            if int(a)>60:
                cnt+=1
        return cnt
        