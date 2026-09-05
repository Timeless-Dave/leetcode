class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<2:
            return s
        start, max_len = 0,1
        for i in range(n):
            l,r = i,i
            while l>= 0 and r<n and s[l] == s[r]:
                curr_len = r-l+1
                if curr_len>max_len:
                    start, max_len = l,curr_len
                l -= 1
                r += 1
            l,r = i, i+1
            while l >= 0 and r<n and s[l] == s[r]:
                curr_len = r-l+1
                if curr_len > max_len:
                    start, max_len = l, curr_len
                l -= 1
                r += 1
        return s[start:max_len+start]