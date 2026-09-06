class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [[] for _ in range(numRows)]
        cur, direction = 0, 1
        for c in s:
            rows[cur].append(c)
            if cur == 0:
                direction = 1
            elif cur == numRows - 1:
                direction = -1
            cur += direction
        return ''.join(''.join(r) for r in rows)