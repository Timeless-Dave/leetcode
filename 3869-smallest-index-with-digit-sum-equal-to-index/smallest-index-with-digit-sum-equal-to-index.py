class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        # We only need to check up to index 27. 
        # Max digit sum for numbers <= 1000 is 27 (from 999).
        limit = min(len(nums), 28)
        
        for i in range(limit):
            num = nums[i]
            digit_sum = 0
            
            # Fast mathematical digit extraction
            while num > 0:
                digit_sum += num % 10
                num //= 10
                
            if digit_sum == i:
                return i
                
        return -1