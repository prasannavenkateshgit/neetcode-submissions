class Solution:
    def isPalindrome(self, s: str) -> bool:
        copy=""
        for i in range(len(s)):
            if s[i].isalnum():
                copy+=s[i].lower()
        i=0
        j=len(copy)-1
        while i<j:
            if copy[i]!=copy[j]:
                return False
            i+=1
            j-=1
        return True
        