class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sorted_nums = sorted(nums)
        
        left, right = 0, len(sorted_nums) - 1
        
        while left < right:
            current_sum = sorted_nums[left] + sorted_nums[right]
            
            if current_sum == target:
                index1 = nums.index(sorted_nums[left])
                index2 = nums.index(sorted_nums[right])
                if index1 == index2:
                    index2 = nums.index(sorted_nums[right], index1+1)
                return [index1, index2]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []