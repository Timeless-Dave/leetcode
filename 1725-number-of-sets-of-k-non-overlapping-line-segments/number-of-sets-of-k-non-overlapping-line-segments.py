class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        pre = [1] * n
        # f = [1]*(n+1)
        # g=list(range(n+1))
        for _ in range(1, k+1):
            dp = [0]*(n)
            cur = [0]*(n)
            for i in range(1, n):
                dp[i]= (dp[i-1] + pre[i-1]) % mod
                cur[i] = (cur[i-1] + dp[i]) % mod
            pre = cur
        return pre[n-1]