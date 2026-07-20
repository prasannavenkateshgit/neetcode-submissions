class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float('inf')
        left=0
        currsum=0
        for r in range(len(nums)):
            currsum+=nums[r]
            if currsum>=target:
                ans=min(ans,r-left+1)
            while currsum>=target:
                currsum-=nums[left]
                left+=1
                if currsum>=target:
                    ans=min(ans,r-left+1)
        return ans if ans<float('inf') else 0
        