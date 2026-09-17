class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        left_min = [float('inf')] * n
        best = float('inf')
        ans = float('inf')
        curr_sum = 0
        l = 0
        for r in range(n):
            curr_sum += arr[r]
            while curr_sum > target:
                curr_sum -= arr[l]
                l += 1
            if curr_sum == target:
                curr_len = r-l+1
                if l > 0 and left_min[l-1] < float('inf'):
                    ans = min(ans, curr_len + left_min[l-1])
                best = min(best, curr_len)
            left_min[r] = best
        return ans if ans < float('inf') else -1