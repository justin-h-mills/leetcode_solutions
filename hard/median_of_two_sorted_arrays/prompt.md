# **[Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)**


## **Prompt:**

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log(m+n))`.

### **Example 1:**

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

### **Example 2:**

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

### **Constraints**

* $nums1.length == m$

* $nums2.length == n$

* $0 <= m <= 1000$

* $0 <= n <= 1000$

* $1 <= m + n <= 2000$

* $-10^6 <= nums1[i], nums2[i] <= 10^6$

### **initial code:**

``` python
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
```

<br>

## **Binary Search**

This solution starts by ensuring that nums1 is the smaller array and then uses a binary search approach to find the median of two sorted arrays nums1 and nums2.

### **Pseudocode**

```
1. If the length of nums1 is greater than the length of nums2, swap nums1 and nums2.
2. Get the lengths of nums1 (m) and nums2 (n).
3. Initialize imin to 0 and imax to m.
4. Calculate half_len as (m + n + 1) // 2.
5. While imin is less than or equal to imax:
    a. Calculate i as (imin + imax) // 2.
    b. Calculate j as half_len - i.
    c. Check if i is less than m and if nums2[j - 1] is greater than nums1[i]:
        - Update imin to i + 1.
    d. Otherwise, check if i is greater than 0 and if nums1[i - 1] is greater than nums2[j]:
        - Update imax to i - 1.
    e. If neither of the above conditions is met, calculate:
        - max_of_left as the maximum of nums1[i - 1] and nums2[j - 1].
        - If (m + n) is odd, return max_of_left as the median.
        - Calculate min_of_right as the minimum of nums1[i] and nums2[j].
        - Return the average of max_of_left and min_of_right as the median.
```

### **Solution Code**

``` python
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Ensure nums1 is the smaller array
        
        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            if i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0: max_of_left = nums2[j - 1]
                elif j == 0: max_of_left = nums1[i - 1]
                else: max_of_left = max(nums1[i - 1], nums2[j - 1])
                
                if (m + n) % 2 == 1:
                    return float(max_of_left)
                
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                
                return (max_of_left + min_of_right) / 2.0
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(log(m+n))$, where m and n are the lengths of the two arrays.

* Space Complexity: $O(1)$

<br>

## **Brute Force**

This solution merges the two input arrays, sorts the merged array, and calculates the median based on whether the total number of elements is even or odd.

### **Pseudocode**

```
1. Merge the two input arrays nums1 and nums2 into a new array merged.
2. Sort the merged array.
3. Calculate the length n of the merged array.
4. If n is even:
    a. Calculate mid as n // 2.
    b. Return the average of merged[mid - 1] and merged[mid] as the median.
5. If n is odd:
    a. Return merged[n // 2] as the median.
```

### **Solution Code**

``` python
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
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(m + n), $where m and n are the lengths of the two arrays.

* Space Complexity: $O(m + n)$, $where m and n are the lengths of the two arrays.

<br>

## **Divide and Conquer**

Similar to the binary search solution, this one also ensures that nums1 is the smaller array and uses a divide and conquer approach to find the median.

### **Pseudocode**

```
1. Ensure that nums1 is the smaller array by swapping if necessary.
2. Get the lengths of nums1 (m) and nums2 (n).
3. Calculate imin as 0, imax as m, and half_len as (m + n + 1) // 2.
4. While imin is less than or equal to imax:
    a. Calculate i as (imin + imax) // 2.
    b. Calculate j as half_len - i.
    c. If i is less than m and nums2[j - 1] is greater than nums1[i]:
        - Update imin to i + 1.
    d. If i is greater than 0 and nums1[i - 1] is greater than nums2[j]:
        - Update imax to i - 1.
    e. If neither of the above conditions is met, calculate:
        - max_of_left as the maximum of nums1[i - 1] and nums2[j - 1].
        - If (m + n) is odd, return max_of_left as the median.
        - Calculate min_of_right as the minimum of nums1[i] and nums2[j].
        - Return the average of max_of_left and min_of_right as the median.
```

### **Solution Code**

``` python
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
    
        m, n = len(nums1), len(nums2)
        
        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            if i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0: max_of_left = nums2[j - 1]
                elif j == 0: max_of_left = nums1[i - 1]
                else: max_of_left = max(nums1[i - 1], nums2[j - 1])
                
                if (m + n) % 2 == 1:
                    return float(max_of_left)
                
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                
                return (max_of_left + min_of_right) / 2.0
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(log(min(m,n)))$, where m and n are the lengths of the two arrays.

* Space Complexity: $O(1)$

<br>

## **Heapq**

This solution merges the input arrays using the heapq.merge() function and calculates the median based on whether the total number of elements is even or odd.

### **Pseudocode**

```
1. Merge the input arrays nums1 and nums2 using the heapq.merge() function, and store the result in the merged list.
2. Calculate the length n of the merged list.
3. If n is even:
    a. Calculate mid as n // 2.
    b. Return the average of merged[mid - 1] and merged[mid] as the median.
4. If n is odd:
    a. Return merged[n // 2] as the median.
```

### **Solution Code**

``` python
import heapq

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = list(heapq.merge(nums1, nums2))
        n = len(merged)
        
        if n % 2 == 0:
            mid = n // 2
            return (merged[mid - 1] + merged[mid]) / 2.0
        else:
            return float(merged[n // 2])
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(log(m+n))$, where m and n are the lengths of the two arrays.

* Space Complexity: $O(m + n)$, where m and n are the lengths of the two arrays.