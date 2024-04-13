class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        tot=0
        n=x
        while x:
            tot+=x%10
            x=x//10
        if n%tot==0:
            return tot
        return -1
        