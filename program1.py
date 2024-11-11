from collections import deque
class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid:
            return 0
        
        rows,cols=len(grid),len(grid[0])
        island_count= 0
        
        def bfs(r,c):
            queue=deque([(r,c)])
            grid[r][c]='W'
            
            while queue:
                row,col =queue.popleft()
                for dr,dc in [(1,0),(-1,0),(0,1), (0, -1)]: 
                    new_row,new_col = row + dr, col + dc
                    if 0<= new_row<rows and 0<=new_col<cols and grid[new_row][new_col]=='L':
                        grid[new_row][new_col]='W' 
                        queue.append((new_row,new_col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='L':
                    island_count+= 1 
                    bfs(r,c)  
        
        return island_count
