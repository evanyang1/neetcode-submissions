class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[0] * cols for _ in range(rows)]
        area = 0

        def traverse(x, y):
            nonlocal area
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return
            if grid[x][y] == 0 or visited[x][y] == 1:
                return
            visited[x][y] = 1
            area += 1
            traverse(x - 1, y)
            traverse(x + 1, y)
            traverse(x, y - 1)
            traverse(x, y + 1)

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    area = 0
                    traverse(i, j)
                    res = max(area, res)
        return res