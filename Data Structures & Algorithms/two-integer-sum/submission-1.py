class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic=defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]],i]
            else:
                dic[target-nums[i]]=i
        
        