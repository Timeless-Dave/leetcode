class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        # pre[i] = number of descents nums[j-1] > nums[j] for 1 <= j <= i
        pre = [0] * n
        for i in range(1, n):
            pre[i] = pre[i - 1] + (nums[i - 1] > nums[i])

        # nxt[j] = smallest index t >= j with nums[t-1] > nums[t] (n if none)
        nxt = [n] * (n + 1)
        for j in range(n - 1, 0, -1):
            nxt[j] = j if nums[j - 1] > nums[j] else nxt[j + 1]

        total = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            prev_max = 0          # nums[i] >= 1
            ok = True
            for s in range(0, n, k):
                e = s + k - 1
                inner = pre[e] - pre[s]
                if inner == 0:                       # already sorted block
                    lo, hi = nums[s], nums[e]
                elif inner == 1 and nums[e] <= nums[s]:  # rotated sorted, no wrap descent
                    p = nxt[s + 1]
                    lo, hi = nums[p], nums[p - 1]
                else:
                    ok = False
                    break
                if lo < prev_max:                    # blocks must chain in order
                    ok = False
                    break
                prev_max = hi
            if ok:
                total += k
        return total