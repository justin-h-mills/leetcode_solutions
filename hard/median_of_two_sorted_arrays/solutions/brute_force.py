class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)
        
        if n % 2 == 0:
            mid = n // 2
            return (merged[mid - 1] + merged[mid]) / 2.0
        else:
            return float(merged[n // 2])