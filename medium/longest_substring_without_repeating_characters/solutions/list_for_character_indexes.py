class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = [-1] * 256  # Assuming ASCII characters
        
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            if char_index[ord(s[end])] >= start:
                start = char_index[ord(s[end])] + 1
            char_index[ord(s[end])] = end
            max_length = max(max_length, end - start + 1)
        
        return max_length