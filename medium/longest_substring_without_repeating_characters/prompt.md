# **[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)**


## **Prompt:**

Given a string `s`, find the length of the **longest substring** without repeating characters.

### **Example 1:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### **Example 2:**

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### **Example 3:**

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

### **Constraints**

* $0 <= s.length <= 5 * 10^4$

* `s` consists of English letters, digits, symbols, and spaces.

**Follow-up:** 

### **initial code:**

``` python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
```

<br>

## **Brute Force**

The Brute Force approach involves systematically checking all possible substrings in the given string to find the longest substring without repeating characters. It maintains two pointers that iterate through the string, and a set to track characters within the current substring.

### **Pseudocode**

```
1. Initialize 'max_length' to 0.
2. Get the length 'n' of the input string 's'.
3. Iterate through 's' from index 0 to n-1:
   a. Initialize an empty set 'seen' to keep track of characters.
   b. Initialize 'length' to 0.
   c. Iterate through 's' from the current index 'i' to the end of the string 'n':
      i. If the character 's[j]' is not in 'seen':
         - Add 's[j]' to the 'seen' set.
         - Increment 'length' by 1.
         - Update 'max_length' to be the maximum of 'max_length' and 'length'.
      ii. If the character 's[j]' is already in 'seen', break the loop.
4. Return 'max_length' as the result.
```

### **Solution Code**

``` python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:    
        max_length = 0
        n = len(s)
        
        for i in range(n):
            seen = set()
            length = 0
            for j in range(i, n):
                if s[j] not in seen:
                    seen.add(s[j])
                    length += 1
                    max_length = max(max_length, length)
                else:
                    break
        
        return max_length
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(n^3)$, where 'n' is the length of the input string.

* Space Complexity: $O(min(n,m))$, where 'n' is the length of the input string, and 'm' is the character set size.

<br>

## **Dynamic Sliding Window**

The Dynamic Sliding Window approach maintains a sliding window of characters, and it adjusts the start position of the window when a repeating character is encountered. It uses a dictionary to track the most recent index of each character, allowing efficient character lookups.

### **Pseudocode**

```
1. Initialize an empty dictionary 'char_index' to store character indices.
2. Initialize 'max_length' to 0.
3. Initialize 'start' to 0.
4. Iterate through the characters in the input string 's':
   a. For each character 's[end]' at index 'end':
      i. Check if 's[end]' is in 'char_index' and the index is greater than or equal to 'start':
         - If true, update 'start' to be one position after the last occurrence of 's[end]'.
      ii. Update the value associated with 's[end]' in 'char_index' to 'end'.
      iii. Calculate 'max_length' as the maximum of the current 'max_length' and 'end - start + 1'.
5. Return 'max_length' as the result.
```

### **Solution Code**

``` python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1
            char_index[s[end]] = end
            max_length = max(max_length, end - start + 1)
        
        return max_length
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(n)$, where 'n' is the length of the input string.

* Space Complexity: $O(min(n,m))$, where 'n' is the length of the input string, and 'm' is the character set size.

<br>

## **Hashset**

The Hashset approach uses a set data structure to keep track of characters within the current substring. When a repeating character is encountered, the algorithm removes characters from the beginning of the substring to ensure there are no repeating characters.

### **Pseudocode**

```
Initialize an empty set 'char_set'
Initialize 'max_length' and 'start' variables
for end in range(len(s)):
    while s[end] is in 'char_set':
        Remove 's[start]' from 'char_set'
        Increment 'start'
    Add 's[end]' to 'char_set'
    Update 'max_length' as max(max_length, end - start + 1)
Return 'max_length'
```

### **Solution Code**

``` python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(s[end])
            max_length = max(max_length, end - start + 1)
        
        return max_length
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(n)$, where 'n' is the length of the input string.

* Space Complexity: $O(min(n,m))$, where 'n' is the length of the input string, and 'm' is the character set size.

<br>

## **List for Character Indexes**

The List for Character Indexes approach uses a list to store the index of the last occurrence of each character. When a repeating character is found, it updates the start position of the window based on the character's last occurrence index. This approach assumes ASCII 

### **Pseudocode**

```
1. Initialize a list 'char_index' of size 256 with all elements set to -1. (Assuming ASCII characters)
2. Initialize 'max_length' to 0.
3. Initialize 'start' to 0.
4. Iterate through the characters in the input string 's':
   a. For each character 's[end]' at index 'end':
      i. Check if the index of 's[end]' in 'char_index' is greater than or equal to 'start':
         - If true, update 'start' to be one position after the last occurrence of 's[end]'.
      ii. Update the index of 's[end]' in 'char_index' to 'end'.
      iii. Calculate 'max_length' as the maximum of the current 'max_length' and 'end - start + 1'.
5. Return 'max_length' as the result.
```

### **Solution Code**

``` python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = [-1] * 256
        
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            if char_index[ord(s[end])] >= start:
                start = char_index[ord(s[end])] + 1
            char_index[ord(s[end])] = end
            max_length = max(max_length, end - start + 1)
        
        return max_length
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(n)$, where 'n' is the length of the input string.

* Space Complexity: $O(1)$, as the space used is constant and does not depend on the input size.

## **Queue**

The Queue approach maintains a queue of characters in the substring, ensuring that no repeating characters are present. It iterates through the input string and appends characters to the queue. If a repeating character is encountered, it removes characters from the beginning of the queue.

### **Pseudocode**

```
1. Check if the input string 's' is an empty string:
   a. If true, return 0 as the result.
2. Initialize an empty list 'substring_queue' to keep track of characters in the current substring.
3. Initialize 'longest' to 1, as the minimum possible length is 1.
4. Iterate through the characters in the input string 's':
   a. For each character 'char' in 's':
      i. While 'char' is in 'substring_queue':
         - Remove the first character from 'substring_queue' (pop the first element).
      ii. Add 'char' to the end of 'substring_queue' to extend the current substring.
      iii. If the length of 'substring_queue' is greater than 'longest':
           - Update 'longest' with the length of 'substring_queue'.
5. Return 'longest' as the result, which represents the length of the longest substring without repeating characters in 's'.
```

### **Solution Code**

``` python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        substring_queue = []
        longest = 1
        for char in s:
            while char in substring_queue:
                substring_queue.pop(0)
            substring_queue.append(char)
            if len(substring_queue) > longest:
                    longest = len(substring_queue)
        return longest
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(n)$, where 'n' is the length of the input string.

* Space Complexity: $O(n)$, where 'n' is the length of the input string.

## **Two Pointers**

The Two Pointers approach uses two pointers to define a sliding window. It iterates through the input string while maintaining the start and end of the substring. When a repeating character is found, it moves the start pointer to the right of the first occurrence of the character.

### **Pseudocode**

```
1. Initialize 'max_length' to 0, which will store the length of the longest substring.
2. Initialize 'start' to 0, which marks the start of the current substring.
3. Initialize 'end' to 0, which marks the end of the current substring.
4. Initialize an empty set 'char_set' to keep track of unique characters in the substring.
5. While 'end' is less than the length of the input string 's':
   a. If the character at index 'end' in 's' is not in 'char_set':
      i. Add the character at index 'end' in 's' to 'char_set'.
      ii. Increment 'end' by 1 to extend the current substring.
      iii. Calculate 'max_length' as the maximum of the current 'max_length' and 'end - start', capturing the length of the substring.
   b. If the character at index 'start' in 's' is already in 'char_set':
      i. Remove the character at index 'start' in 's' from 'char_set'.
      ii. Increment 'start' by 1 to move the start of the substring to the right.
6. Return 'max_length' as the result, representing the length of the longest substring without repeating characters in 's'.
```

### **Solution Code**

``` python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        end = 0
        char_set = set()
        
        while end < len(s):
            if s[end] not in char_set:
                char_set.add(s[end])
                end += 1
                max_length = max(max_length, end - start)
            else:
                char_set.remove(s[start])
                start += 1
        
        return max_length
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(n)$, where 'n' is the length of the input string.

* Space Complexity: $O(min(n,m))$, where 'n' is the length of the input string, and 'm' is the number of unique characters in the string