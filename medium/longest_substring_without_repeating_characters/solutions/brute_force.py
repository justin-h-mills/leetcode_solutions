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
