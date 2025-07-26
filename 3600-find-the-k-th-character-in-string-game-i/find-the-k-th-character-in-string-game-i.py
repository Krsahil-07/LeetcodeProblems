class Solution:
    def kthCharacter(self, k: int) -> str:
        original_word="a"
        while len(original_word)<k:
            str1=copy.deepcopy(original_word)
            for i in range(len(str1)):
                if str1[i]=="z":
                    original_word+="a"
                else:
                    original_word+= chr(ord(str1[i])+1)
        return original_word[k-1]
        