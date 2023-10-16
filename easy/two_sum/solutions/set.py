class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_set = set()
    
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_set:
                return [nums.index(complement), index]
            num_set.add(num)
        
        return []