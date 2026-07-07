class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def bfs(starts, vis):
            q = deque(starts)
            for r, c in starts:
                vis[r][c] = True

            while q:
                r, c = q.popleft()
                h = heights[r][c]
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and not vis[nr][nc]:
                        if heights[nr][nc] >= h:  # reverse flow
                            vis[nr][nc] = True
                            q.append((nr, nc))

        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        pac_starts = [(0, c) for c in range(COLS)] + [(r, 0) for r in range(ROWS)]
        atl_starts = [(ROWS - 1, c) for c in range(COLS)] + [
            (r, COLS - 1) for r in range(ROWS)
        ]

        bfs(pac_starts, pac)
        bfs(atl_starts, atl)

        return [
            [r, c] for r in range(ROWS) for c in range(COLS) if pac[r][c] and atl[r][c]
        ]  