class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        count = 1
        longest = 1
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                count += 1
            elif nums[i + 1] == nums[i]:
                continue
            else:
                count = 1

            longest = max(longest, count)

        return longest
        