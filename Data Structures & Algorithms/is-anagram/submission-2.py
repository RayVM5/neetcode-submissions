class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0]*26 
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                count[ord(s[i].lower())-97]+=1
                count[ord(t[i].lower())-97]-=1
        if count != [0]*26:
            return False
        else:
            return True
