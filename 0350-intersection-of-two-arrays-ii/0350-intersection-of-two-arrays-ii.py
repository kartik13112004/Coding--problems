class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for x in nums2:
            if x in nums1:
                result.append(x)
                nums1.remove(x)
        return result
        