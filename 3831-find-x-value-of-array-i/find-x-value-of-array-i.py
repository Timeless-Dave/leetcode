from typing import List


class Solution:

  def resultArray(self, nums: List[int], k: int) -> List[int]:
    result = [0] * k
    # dp[v] stores the number of subarrays ending at the previous index with product % k == v
    dp = [0] * k

    for num in nums:
      m = num % k
      next_dp = [0] * k

      # 1. Start a new subarray of length 1 with `num`
      next_dp[m] += 1

      # 2. Extend previous subarrays
      for v in range(k):
        if dp[v]:
          next_dp[(v * m) % k] += dp[v]

      # 3. Add counts of all subarrays ending at the current index to result
      for v in range(k):
        result[v] += next_dp[v]

      dp = next_dp

    return result