class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #nums[:] = nums[-k%len(nums):]+nums[:-k%len(nums)] - ONE LINER
        n=len(nums)
        k%=n
        def reverse(l,r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l,r=l+1,r-1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        