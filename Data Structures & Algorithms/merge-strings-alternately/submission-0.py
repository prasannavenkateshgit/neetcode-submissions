class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        alt=0
        i=0
        j=0
        ans=''
        while i<len(word1) and j<len(word2):
            if alt:
                ans+=word2[j]
                alt=0
                j+=1
            else:
                ans+=word1[i]
                alt=1
                i+=1
        while i<len(word1):
            ans+=word1[i]
            i+=1
        while j<len(word2):
            ans+=word2[j]
            j+=1
        return ans
            
        