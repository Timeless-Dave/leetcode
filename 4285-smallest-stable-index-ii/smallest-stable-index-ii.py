from typing import List
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        suffix_min = [0]*n
        suffix_min[n-1]=nums[n-1]
        for i in range(n-2, -1, -1):
            v=nums[i]
            m=suffix_min[i+1]
            suffix_min[i] = v if v< m else m
        prefix_max = -10**18
        for i,v in enumerate(nums):
            if v > prefix_max:
                prefix_max = v
            if prefix_max - suffix_min[i] <= k:
                return i
        return -1