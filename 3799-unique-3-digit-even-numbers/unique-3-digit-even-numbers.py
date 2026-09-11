class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        seen = set()
        n = len(digits)
        for i in range(n):
            d1 = digits[i]
            if d1 == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                d2 = digits[j]
                for k in range(n):
                    if k == i or k == j:
                        continue
                    d3 = digits[k]
                    if d3 % 2:
                        continue
                    seen.add(d1 * 100 + d2 * 10 + d3)
        return len(seen)