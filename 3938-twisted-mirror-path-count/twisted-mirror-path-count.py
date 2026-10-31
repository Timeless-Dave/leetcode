from typing import List
import functools

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        @functools.lru_cache(None)
        def get_landing(r, c, dr, dc):
            curr_r, curr_r_dir = r, dr
            curr_c, curr_c_dir = c, dc
            
            while True:
                if 0 <= curr_r < m and 0 <= curr_c < n and grid[curr_r][curr_c] == 1:
                    if curr_c_dir == 1:  # entered moving right -> turn down
                        curr_r_dir, curr_c_dir = 1, 0
                        curr_r += 1
                    else:                # entered moving down -> turn right
                        curr_r_dir, curr_c_dir = 0, 1
                        curr_c += 1
                else:
                    break
            
            if 0 <= curr_r < m and 0 <= curr_c < n:
                return (curr_r, curr_c)
            return None

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue
                if i == m - 1 and j == n - 1:
                    continue
                
                # Move Right
                landings_right = get_landing(i, j + 1, 0, 1)
                if landings_right:
                    tr, tc = landings_right
                    dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD
                
                # Move Down
                landings_down = get_landing(i + 1, j, 1, 0)
                if landings_down:
                    tr, tc = landings_down
                    dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD
                        
        return dp[m - 1][n - 1]