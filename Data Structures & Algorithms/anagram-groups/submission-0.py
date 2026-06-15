class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for s in strs:
            temp=sorted(s)
            temp="".join(temp)
            dic[temp].append(s)
        ans=[]
        for k,v in dic.items():
            ans.append(v)
        return ans
        