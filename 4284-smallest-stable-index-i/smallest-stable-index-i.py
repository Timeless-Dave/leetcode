class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        pre_max = [0]*n
        current_max = nums[0]
        for i, v in enumerate(nums):
            if v > current_max:
                current_max = v
            pre_max[i] = current_max
        suf_min = [0]*n
        current_min = nums[-1]
        for i in range(n-1, -1, -1):
            if nums[i] < current_min:
                current_min = nums[i]
            suf_min[i] = current_min
        for i in range(n):
            if pre_max[i] - suf_min[i] <= k:
                return i
        return -1