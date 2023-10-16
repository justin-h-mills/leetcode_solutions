# **[Two Sum](https://leetcode.com/problems/two-sum/)**


## **Prompt:**

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

### **Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### **Example 2:**

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### **Example 3:**

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

### **Constraints**

* $2 <= nums.length <= 10^4$

* $-10^9 <= nums[i] <= 10^9$

* $-10^9 <= target <= 10^9$

* **Only one valid answer exists.**

**Follow-up:** Can you come up with an algorithm that is less than $O(n^2)$ time complexity?

### **initial code:**

``` python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
```

<br>

## **Brute Force**

The Brute Force solution involves using two nested loops to iterate through the array, comparing each pair of elements to check if their sum equals the target.

### **Pseudocode**

```
For i in range(0, length of nums):
    For j in range(i + 1, length of nums):
        If nums[i] + nums[j] equals target:
            Return [i, j]
Return an empty list if no pairs are found
```

### **Solution Code**

``` python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(n^2)$

* Space Complexity: $O(1)$

<br>

<br>

## **Hashmap (Dictionary)**

The Hashmap solution uses a dictionary (hashmap) to efficiently store elements and their indices while iterating through the array. For each element, it calculates the complement needed to reach the target and checks if it exists in the dictionary.

### **Pseudocode**

```
Create an empty dictionary called num_dict
For each element num at index in nums
    Calculate the complement as target - num
    If complement exists in num_dict
        Return [num_dict[complement], index]
    Store num in num_dict with its index
Return an empty list if no pairs are found
```

### **Solution Code**

``` python
class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
    
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], index]
            num_dict[num] = index
        
        return []
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(n)$

* Space Complexity: $O(n)$

<br>

## **Set**

The Set solution involves iterating through the array while storing elements in a set. For each element, it calculates the complement by subtracting it from the target and checks if the complement exists in the set.

### **Pseudocode**

```
Create an empty set called num_set
For each element num at index in nums
    Calculate the complement as target - num
    If complement exists in num_set
        Return [index of complement, index]
    Add num to num_set
Return an empty list if no pairs are found
```

### **Solution Code**

``` python
class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_set = set()
    
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_set:
                return [nums.index(complement), index]
            num_set.add(num)
        
        return []
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(n)$

* Space Complexity: $O(n)$

<br>

## **Two Pointers**

The Two Pointers solution first sorts the array and then initializes two pointers, one at the beginning and one at the end. The pointers are moved towards each other based on whether the sum of the elements at the pointers is greater or smaller than the target.

### **Pseudocode**

```
Sort the nums array in ascending order and store it as sorted_nums
Initialize two pointers, left and right, at the beginning and end of sorted_nums
While left is less than right
    Calculate current_sum as the sum of sorted_nums[left] and sorted_nums[right]
    If current_sum equals target
        Find the indices of sorted_nums[left] and sorted_nums[right] in the original nums array
        If both indices are the same, find the index of the second occurrence of the number in nums
        Return the indices [index1, index2]
    If current_sum is less than target, increment left
    If current_sum is greater than target, decrement right
Return an empty list if no pairs are found
```

### **Solution Code**

``` python
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
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(n * log(n))$ due to the sorting step

* Space Complexity: $O(n)$ for the sorted array

***