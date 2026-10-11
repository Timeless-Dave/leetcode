class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        # Iterate 1-based indices i from 1 to n
        return sum(nums[i - 1] ** 2 for i in range(1, n + 1) if n % i == 0)