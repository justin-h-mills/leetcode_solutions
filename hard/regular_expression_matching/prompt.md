# **[Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)**


## **Prompt:**

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:

* `'.'` Matches any single character.

* `'*'` Matches zero or more of the preceding element.

The matching should cover the **entire** input string (not partial).

### **Example 1:**

```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".`
```

### **Example 2:**

```
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

### **Example 3:**

```
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```

### **Constraints**

* $1 <= s.length <= 20$

* $1 <= p.length <= 20$

* `s` contains onl lowercase English letters.

* `p` contains only lowercase English letters, `'.'`, and `'*'`.

* It is guaranteed for each appearance of the character `'*'`, there will be a previous valid character to match.

### **initial code:**

``` python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
```

<br>

## **Dynamic_programming**

In this solution, we create a dynamic programming matrix 'dp' where each cell (i, j) represents whether the substring of 's' from 0 to i matches the pattern 'p' from 0 to j. We initialize 'dp[0][0]' to True since an empty 's' matches an empty 'p'. We then iterate through 'p' to handle cases where asterisks '*' can match zero preceding elements. Finally, we iterate through both 's' and 'p' and use the values in 'dp' to determine if 's' matches 'p'.

### **Pseudocode**

```
1. Create a two-dimensional array 'dp' of size (len(s) + 1) by (len(p) + 1), initialized with False values.
2. Set 'dp[0][0]' to True, indicating that an empty 's' matches an empty 'p'.
3. Iterate through the characters in 'p':
   a. For each character 'p[i]' at index 'i':
      i. Check if 'p[i]' is an asterisk '*' and 'dp[0][i - 1]' is True:
         - If true, set 'dp[0][i + 1]' to True, indicating that 'p[i]' can match an empty string.
4. Iterate through the characters in 's':
   a. For each character 's[i]' at index 'i':
      b. Iterate through the characters in 'p':
         i. For each character 'p[j]' at index 'j':
            - Check if 'p[j]' is equal to 's[i]' or 'p[j]' is a period '.':
               - If true, set 'dp[i + 1][j + 1]' to 'dp[i][j]'.
            - Check if 'p[j]' is an asterisk '*':
               - If true, set 'dp[i + 1][j + 1]' to 'dp[i + 1][j - 1]' or ('p[j - 1]' is equal to 's[i]' or 'p[j - 1]' is a period '.') and 'dp[i][j + 1]'.
5. Return 'dp[len(s)][len(p)]', which indicates whether 's' matches 'p' according to the dynamic programming matrix 'dp'.
```

### **Solution Code**

``` python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True

        for i in range(len(p)):
            if p[i] == '*' and dp[0][i - 1]:
                dp[0][i + 1] = True

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == s[i] or p[j] == '.':
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == '*':
                    dp[i + 1][j + 1] = dp[i + 1][j - 1] or (p[j - 1] == s[i] or p[j - 1] == '.') and dp[i][j + 1]

        return dp[len(s)][len(p)]
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(m * n)$, where m is the length of string 's' and n is the length of pattern 'p'.

* Space Complexity: $O(m * n)$, where m is the length of string 's' and n is the length of pattern 'p'.

<br>

## **Memoization with Recursion**

In this solution, we use a recursive function 'dp(i, j)' to check if 's' and 'p' match starting from the ith character in 's' and the jth character in 'p'. We memoize (store) previously computed results to avoid redundant calculations. The function considers cases where characters match directly or when an asterisk '*' can match zero or more preceding characters. The result of 'dp(0, 0)' tells us if 's' matches 'p'. This solution uses recursion and memoization to efficiently explore all possibilities.

### **Pseudocode**

```
1. Create an empty dictionary 'memo' to store already computed results.
2. Define a recursive function 'dp(i, j)' that takes two parameters 'i' and 'j':
   a. Check if a tuple '(i, j)' is in 'memo':
      i. If true, return the stored result 'memo[(i, j)]'.
   b. Check if 'j' is equal to the length of 'p':
      i. If true, set 'ans' to whether 'i' is equal to the length of 's'.
      ii. If false, proceed to the next steps.
   c. Initialize 'first_match' as 'i' is less than the length of 's' and either 's[i]' is equal to 'p[j]' or 'p[j]' is a period '.'.
   d. Check if 'j + 1' is less than the length of 'p' and 'p[j + 1]' is an asterisk '*':
      i. If true, set 'ans' to the logical OR of two conditions:
         - Calling 'dp(i, j + 2)' recursively (skipping the current character and the asterisk) or
         - Checking 'first_match' and calling 'dp(i + 1, j)' recursively (moving to the next character in 's' and continuing with the same character in 'p').
   e. If the character at 'p[j]' is not an asterisk, set 'ans' to 'first_match' and call 'dp(i + 1, j + 1)' recursively.
   f. Store 'ans' in 'memo[(i, j)]'.
   g. Return 'ans'.
3. Call 'dp(0, 0)' with initial values 'i' and 'j' to perform the dynamic programming matching.
4. Return the result of 'dp(0, 0)' as the final result of the isMatch function.
```

### **Solution Code**

``` python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                ans = i == len(s)
            else:
                first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
                if j + 1 < len(p) and p[j + 1] == '*':
                    ans = (dp(i, j + 2) or
                           (first_match and dp(i + 1, j)))
                else:
                    ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(m * n)$, where m is the length of string 's' and n is the length of pattern 'p'.

* Space Complexity: $O(m * n)$, where m is the length of string 's' and n is the length of pattern 'p'.