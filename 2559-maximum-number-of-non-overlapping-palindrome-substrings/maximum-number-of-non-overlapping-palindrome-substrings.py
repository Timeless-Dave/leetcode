class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        pal_ends = [[] for _ in range(n)]
        for center in range(n):
            l = r = center
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    pal_ends[r].append(l)
                l -= 1
                r += 1
            l, r = center, center +1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l +1 >= k:
                    pal_ends[r].append(l)
                l -= 1
                r += 1
        dp = [0]*n
        for i in range(n):
            if i > 0:
                dp[i] = dp[i-1]
            for start in pal_ends[i]:
                dp[i] = max(dp[i], (dp[start - 1] if start > 0 else 0) + 1)
        return dp[-1]
                