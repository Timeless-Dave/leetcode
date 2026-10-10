from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        
        if sum(diffs) <= k:
            return 0
            
        count = Counter(diffs)
        unique_diffs = sorted(count.keys(), reverse=True)
        
        for i, d in enumerate(unique_diffs):
            if d == 0:
                break
                
            freq = count[d]
            # If this is not the last unique difference, we can see how far we can pull `d` down 
            # towards the next smaller difference `next_d` using `k` operations.
            next_d = unique_diffs[i + 1] if i + 1 < len(unique_diffs) else 0
            
            # The drop required to reach the next difference level for all elements in this group
            diff_drop = d - next_d
            total_ops_needed = freq * diff_drop
            
            if k >= total_ops_needed:
                # We have enough operations to bring all elements in `d` down to `next_d`
                k -= total_ops_needed
                count[next_d] += freq
                count[d] = 0
            else:
                # We don't have enough operations to reach `next_d` for all elements.
                # Distribute whatever operations we have evenly across the elements of this group.
                full_steps = k // freq
                remainder = k % freq
                
                count[d] -= freq
                count[d - full_steps] += freq - remainder
                count[d - full_steps - 1] += remainder
                k = 0
                break
                
        if k > 0:
            return 0
            
        result = 0
        for d, freq in count.items():
            result += freq * (d ** 2)
            
        return result