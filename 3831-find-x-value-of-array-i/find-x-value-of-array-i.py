from typing import List


class Solution:

  def resultArray(self, nums: List[int], k: int) -> List[int]:
    dp = [0] * k
    result = [0] * k

    for num in nums:
      m = num % k
      new_dp = [0] * k

      # Extend existing subarrays ending at the previous element
      for r in range(k):
        cnt = dp[r]
        if cnt:
          new_dp[(r * m) % k] += cnt

      # Start a new subarray with the current element
      new_dp[m] += 1
      dp = new_dp

      # Accumulate all subarrays ending at the current element
      for r in range(k):
        result[r] += dp[r]

    return result