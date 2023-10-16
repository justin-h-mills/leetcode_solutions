# **[Palindrome Number](https://leetcode.com/problems/palindrome-number/)**


## **Prompt:**

Given an integer `x` return `true` if `x` is a palindrome, and `false` otherwise.

**Palindrome:** An integer is a palindrome when it reads the same forward and backward.

### **Example 1:**

```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

### **Example 2:**

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

### **Example 3:**

```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

### **Constraints**

* $-2^31 <= x <= 2^31 - 1$

**Follow-up:** Could you solve it without converting the integer to a string?

### **initial code:**

``` python
class Solution:
    def isPalindrome(self, x: int) -> bool:
```

<br>

## **Compare Half of Integer**

This approach checks whether an integer is a palindrome by reversing only half of the integer and comparing it with the other half. It handles cases where the integer has an odd number of digits.

### **Pseudocode**

```
1. Check if the input integer 'x' is negative or has a last digit of 0 but is not equal to 0:
   a. If true, return False, as these conditions make it impossible for 'x' to be a palindrome.
2. Initialize 'reversed_half' to 0, which will store the reversed half of 'x'.
3. While 'x' is greater than 'reversed_half':
   a. Multiply 'reversed_half' by 10 and add the last digit of 'x' to it.
   b. Update 'x' by integer division by 10, effectively removing the last digit.
4. Check if 'x' is equal to 'reversed_half' or 'x' is equal to 'reversed_half' divided by 10:
   a. If true, return True, indicating that 'x' is a palindrome.
   b. If false, return False.
```

### **Solution Code**

``` python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(log10(x))$

* Space Complexity: $O(1)$

where x is the number of digits in input integer.

<br>

## **Convert to String**

This solution converts the integer to a string and checks if the string is equal to its reverse. It's a straightforward method but involves string manipulation.

### **Pseudocode**

```
1. Convert the input integer 'x' to a string using str(x).
2. Reverse the string obtained in step 1 using slicing with [::-1].
3. Check if the reversed string is equal to the original string:
   a. If true, return True, indicating that 'x' is a palindrome.
   b. If false, return False.
```

### **Solution Code**

``` python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(log10(x))$

* Space Complexity: $O(log10(x))$

where x is the number of digits in input integer.

<br>

## **Mathematical Reversal**

In this approach, the integer is reversed mathematically by repeatedly extracting and adding digits. It then compares the reversed integer with the original to check for a palindrome.

### **Pseudocode**

```
1. Check if the input integer 'x' is less than 0:
   a. If true, return False, as negative numbers are not palindromes.
2. Initialize 'reversed_x' to 0, which will store the reversed form of 'x'.
3. Create a variable 'original_x' to store the original value of 'x'.
4. While 'x' is greater than 0:
   a. Multiply 'reversed_x' by 10 and add the last digit of 'x' to it.
   b. Update 'x' by integer division by 10, effectively removing the last digit.
5. Check if 'original_x' is equal to 'reversed_x':
   a. If true, return True, indicating that 'x' is a palindrome.
   b. If false, return False.
```

### **Solution Code**

``` python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_x = 0
        original_x = x

        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

        return original_x == reversed_x
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(log10(x))$

* Space Complexity: $O(1)$

where x is the number of digits in input integer.

<br>

## **Stack**

This solution uses a stack to push each digit of the integer onto the stack. It then pops the digits from the stack and compares them with the original integer to check for palindromes.

### **Pseudocode**

```
1. Check if the input integer 'x' is less than 0:
   a. If true, return False, as negative numbers are not palindromes.
2. Create a variable 'original_x' and set it to 'x' to store the original value of 'x'.
3. Initialize an empty stack 'stack' to store the digits of 'x'.
4. While 'x' is greater than 0:
   a. Calculate the last digit of 'x' using 'x % 10'.
   b. Push the last digit onto the 'stack'.
   c. Update 'x' by integer division by 10, effectively removing the last digit.
5. While 'stack' is not empty:
   a. Pop the top element from 'stack'.
   b. Compare it to the last digit of 'original_x':
      i. If they are not equal, return False, indicating that 'x' is not a palindrome.
      ii. If they are equal, continue to the next digit by updating 'original_x' with integer division by 10.
6. Return True, indicating that 'x' is a palindrome if the loop completes without returning False.
```

### **Solution Code**

``` python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original_x = x
        stack = []

        while x > 0:
            stack.append(x % 10)
            x //= 10

        while stack:
            if stack.pop() != original_x % 10:
                return False
            original_x //= 10

        return True
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(log10(x))$

* Space Complexity: $O(log10(x))$

where x is the number of digits in input integer.