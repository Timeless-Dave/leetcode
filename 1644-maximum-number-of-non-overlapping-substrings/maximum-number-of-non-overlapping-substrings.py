class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        # first = {c: n for c in s}
        # last = {}
        # for i, c in enumerate(s):
        #     first[c] = min(first[c], i)
        #     last[c] = i
        # candidates = []
        # for c in first:
        #     start = first[c]
        #     end = last[c]
        #     i = start
        #     valid = True
        #     while i <= end:
        #         ci = s[i]
        #         if first[ci] < start:
        #             valid = False
        #             break
        #         end = max(end, last[ci])
        #         i += 1
        #     if valid:
        #         candidates.append((end, start))
        #     candidates.sort()
        #     res = []
        #     prev_end = -1
        #     for end, start in candidates:
        #         if start > prev_end:
        #             res.append(s[start:end+1])
        #             prev_end = end
        #     return res
        L = [n]*26
        R = [-1]*26
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            L[idx] = min(L[idx], i)
            R[idx] = max(R[idx], i)
        candidates = []
        for c in range(26):
            if L[c] <= R[c]:
                start, end = L[c], R[c]
                j = start
                valid = True
                while j <= end:
                    d = ord(s[j]) - ord('a')
                    if L[d] < start:
                        valid = False
                        break
                    end = max(end, R[d])
                    j += 1
                if valid:
                    candidates.append((end, start))
        candidates.sort()
        res = []
        prev_end = -1
        for end, start in candidates:
            if start > prev_end:
                res.append(s[start:end+1])
                prev_end = end
        return res
                