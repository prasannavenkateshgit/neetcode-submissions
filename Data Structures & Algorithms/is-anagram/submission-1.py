class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1=defaultdict(int)
        dic2=defaultdict(int)
        for i in s:
            dic1[i]+=1
        for j in t:
            dic2[j]+=1
        for k,v in dic1.items():
            if k not in dic2:
                return False
            else:
                if v!=dic2[k]:
                    return False
        for k,v in dic2.items():
            if k not in dic1:
                return False
            else:
                if v!=dic1[k]:
                    return False
        return True
        