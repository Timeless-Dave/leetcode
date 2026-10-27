from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    # BFS or DFS traversal for the component
                    island_sum = 0
                    queue = [(r, c)]
                    island_sum += grid[r][c]
                    grid[r][c] = 0  # Mark as visited
                    
                    while queue:
                        cr, cc = queue.pop(0) # or use a pointer for efficiency, or DFS with stack.pop()
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0  # Mark as visited
                                queue.append((nr, nc))
                                
                    if island_sum % k == 0:
                        count += 1
                        
        return count