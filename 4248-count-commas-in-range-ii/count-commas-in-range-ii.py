class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        k=1
        while True:
            start = 10 ** (3*k)
            if start > n:
                break
            end = min(n, 10 ** (3 * k + 3)-1)
            ans += (end - start + 1) * k
            k += 1
        return ans