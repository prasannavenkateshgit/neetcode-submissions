class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        for n in nums:
            dic[n]+=1
            if dic[n]>len(nums)//2:
                return n
        