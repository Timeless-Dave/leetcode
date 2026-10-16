class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        # Generate all possible subarrays
        for i in range(n):
            distinct_elements = set()
            for j in range(i, n):
                distinct_elements.add(nums[j])
                # Add the square of the distinct count of the current subarray
                total_sum += len(distinct_elements) ** 2
                
        return total_sum