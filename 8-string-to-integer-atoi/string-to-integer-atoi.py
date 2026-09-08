class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        while i < n and s[i] == ' ':
            i += 1
        sign = 1
        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1
        res = 0
        max_int = 2**31 - 1
        min_int = -(2**31)
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            if res > max_int // 10 or (res == max_int // 10 and digit > max_int % 10):
                return max_int if sign == 1 else min_int
            res = res * 10 + digit
            i += 1
        return sign * res
        