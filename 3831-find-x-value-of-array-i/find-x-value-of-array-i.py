from typing import List
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        dp = [0]*k
        result = [0]*k
        for num in nums:
            m = num % k
            new_dp = [0] * k
            for r in range(k):

                cnt = dp[r]
                if cnt:
                    new_dp[(r*m) % k] += cnt
            new_dp[m] += 1
            dp = new_dp
            for r in range(k):
                result[r] += dp[r]
        return result