from collections import Counter
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]
        shifts = Counter()
        max_overlap = 0
        for i1, j1 in ones1:
            for i2, j2 in ones2:
                delta = (i2 - i1, j2 - j1)
                shifts[delta] += 1
                if shifts[delta] > max_overlap:
                    max_overlap = shifts[delta]
        return max_overlap
