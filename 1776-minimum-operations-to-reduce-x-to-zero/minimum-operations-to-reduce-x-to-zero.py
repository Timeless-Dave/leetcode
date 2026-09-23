class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        current = 0
        left = 0
        max_len = -1
        for right, val in enumerate(nums):
            current += val
            while current > target and left <= right:
                current -= nums[left]
                left += 1
            if current == target:
                max_len = max(max_len, right - left + 1)
        return len(nums) - max_len if max_len != -1 else -1