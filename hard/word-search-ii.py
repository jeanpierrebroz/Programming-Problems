#unoptimized
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        max_len = 0
        for word in words:
            max_len = max(max_len, len(word))

        words = set(words)

        result = []

        def dfs(i, j, path, used):

            nonlocal max_len

            p = ''.join(path)
            if len(p) > max_len:
                return
            elif p in words:
                result.append(p)
                words.remove(p)

            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and not used[ni][nj]:
                    used[ni][nj] = True
                    path.append(board[ni][nj])
                    dfs(ni, nj, path, used)
                    path.pop()
                    used[ni][nj] = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                u = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                u[i][j] = True
                dfs(i, j, [board[i][j]], u)
        
        return result
        

