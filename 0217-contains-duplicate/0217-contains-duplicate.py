class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s=set()
        for i in range (len(nums)):
            s.add(nums[i])
            if len(s)==len(nums):
                return False 
        return True
  
        
        