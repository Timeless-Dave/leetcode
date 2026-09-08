class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 -1
        INT_MIN = -2**31
        sign = 1 if x >= 0 else -1
        x = x * sign
        result = 0
        while x:
            pop = x % 10
            x //= 10
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and pop > INT_MAX % 10):
                return 0
            result = result * 10 + pop
        return result * sign