class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=0
        max_sum=float("-inf")
        for i in range (len(nums)):
            current_sum=max(nums[i],current_sum+nums[i])
            max_sum=max(max_sum,current_sum)
        return max_sum
        