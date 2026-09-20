class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for idx, ch in enumerate(s, 1):
            weight = ord('z') - ord(ch) + 1
            total += idx * weight
        return total