class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
        idx=0
        for j in range(dic[0]):
            nums[idx]=0
            idx+=1
        for j in range(dic[1]):
            nums[idx]=1
            idx+=1
        for j in range(dic[2]):
            nums[idx]=2
            idx+=1
            
        