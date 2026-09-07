class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 +7
        n = len(s)
        dp = [0]*(n+1)
        dp[0]=1
        last = {}
        for i, ch in enumerate(s,1):
            dp[i]=dp[i-1]*2 %mod
            if ch in last:
                dp[i]= (dp[i] - dp[last[ch]-1]) %mod
            last[ch]=i
        return (dp[n]-1)% mod