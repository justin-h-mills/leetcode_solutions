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