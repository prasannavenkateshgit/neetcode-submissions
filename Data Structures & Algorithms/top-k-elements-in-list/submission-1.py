from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
        reverse=defaultdict(list)
        for key,v in dic.items():
            reverse[v].append(key)
        maxheap=[]
        for key,v in dic.items():
            heappush(maxheap,v)
            if len(maxheap)>k:
                heappop(maxheap)
        ans=[]
        for i in maxheap:
            for j in reverse[i]:
                if j not in ans:
                    ans.append(j)
        return ans

        