class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Count the number of set bits in each position (0 to 29)
        cnt = [0] * 30
        for x in nums:
            for b in range(30):
                if (x >> b) & 1:
                    cnt[b] += 1
        
        # Build the k largest numbers greedily and sum their squares
        total_sum = 0
        for i in range(k):
            current_num = 0
            for b in range(30):
                if cnt[b] > i:
                    current_num |= (1 << b)
            total_sum = (total_sum + current_num * current_num) % MOD
            
        return total_sum