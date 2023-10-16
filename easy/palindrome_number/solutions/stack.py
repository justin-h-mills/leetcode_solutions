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
