from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        ints = [(l,r,w,i) for i, (l,r,w) in enumerate(intervals)]
        ints.sort(key=lambda x: x[0])
        starts = [ints[i][0] for i in range(n)]
        nextIdx = [0] * n
        for i in range(n):
            nextIdx[i] = bisect_right(starts, ints[i][1])
        dpPrev = [(0, ()) for _ in range(n+1)]
        bestAt0 = [(0, ())]
        for _ in range(1, 5):
            dpCurr = [(0, ()) for _ in range(n+1)]
            for i in range(n-1, -1, -1):
                skip = dpCurr[i+1]
                w = ints[i][2]
                nxt = dpPrev[nextIdx[i]]
                takeWeight = w + nxt[0]
                takeList = tuple(sorted(nxt[1] + (ints[i][3],)))
                if takeWeight > skip[0] or (takeWeight == skip[0] and takeList < skip[1]):
                    dpCurr[i] = (takeWeight, takeList)
                else:
                    dpCurr[i] = skip
            bestAt0.append(dpCurr[0])
            dpPrev = dpCurr
        best = bestAt0[0]
        for wt, lst in bestAt0[1:]:
            if wt > best[0] or (wt == best[0] and lst < best[1]):
                best = (wt, lst)
        return list(best[1])