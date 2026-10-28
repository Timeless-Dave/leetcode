class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] will store a set of all possible XOR path values to cell (i, j)
        dp = [set() for _ in range(n)]
        
        # Initialize the starting cell
        dp[0] = {grid[0][0]}
        
        for i in range(m):
            next_dp = [set() for _ in range(n)]
            for j in range(n):
                # Gather possible XOR values from the cell above and the cell to the left
                prev_vals = set()
                if i > 0:
                    prev_vals.update(dp[j])
                if j > 0:
                    prev_vals.update(next_dp[j - 1])
                if i == 0 and j == 0:
                    prev_vals.add(0) # handled by initialization
                
                # Compute new possible XOR values for the current cell
                current_vals = set()
                for val in prev_vals:
                    current_vals.add(val ^ grid[i][j])
                
                next_dp[j] = current_vals
            dp = next_dp
            
        # The answer is the minimum XOR value found at the bottom-right cell (n - 1)
        return min(dp[n - 1])