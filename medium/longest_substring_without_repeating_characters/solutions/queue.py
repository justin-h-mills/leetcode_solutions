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