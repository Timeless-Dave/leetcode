class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            # every arrangement of size ≤ 2 is both an inc and dec rotation
            return 0 if nums[0] == 0 else 1

        first = nums[0]
        inc = dec = True
        for i in range(1, n):
            prev, cur = nums[i - 1], nums[i]
            if inc and cur != (prev + 1) % n:
                inc = False
            if dec and cur != (prev - 1) % n:
                dec = False
            if not inc and not dec:
                return -1

        if inc:
            s = first
            return min((n - s) % n, s + 2)

        # dec: element n-1 sits at index m, and nums[i] = (first - i) mod n
        m = (first - (n - 1)) % n
        return min(m + 1, (n - m) % n + 1)