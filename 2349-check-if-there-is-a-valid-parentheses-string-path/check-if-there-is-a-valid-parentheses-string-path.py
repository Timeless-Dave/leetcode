class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # A valid parentheses string must have an even length.
        # The path length in a grid from (0,0) to (m-1,n-1) is exactly m + n - 1.
        if (m + n - 1) % 2 != 0:
            return False
            
        # A valid string cannot start with ')' or end with '('
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
            
        memo = {}
        
        def dfs(r, c, balance):
            # If out of bounds, this path is invalid
            if r == m or c == n:
                return False
                
            # Update balance based on the current cell
            balance += 1 if grid[r][c] == '(' else -1
            
            # If balance drops below 0, there are more ')' than '(', which is invalid
            if balance < 0:
                return False
                
            # If we reached the target cell, it's valid only if balance is exactly 0
            if r == m - 1 and c == n - 1:
                return balance == 0
                
            # Check memoization dictionary
            state = (r, c, balance)
            if state in memo:
                return memo[state]
                
            # Explore down and right
            ans = dfs(r + 1, c, balance) or dfs(r, c + 1, balance)
            
            memo[state] = ans
            return ans
            
        return dfs(0, 0, 0)