class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        open_count = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                open_count += 1
                i += 1
            else:
                # Check if we have two consecutive ')'
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    # Single ')' needs one inserted ')' to become '))'
                    ans += 1
                    i += 1
                
                # Match with an open '(' if available, else insert '('
                if open_count > 0:
                    open_count -= 1
                else:
                    ans += 1
                    
        # Any remaining '(' needs two ')'s
        ans += open_count * 2
        return ans