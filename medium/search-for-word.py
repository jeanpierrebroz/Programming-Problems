class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool: 
        visiting = set()

        def get_valid_neighbors(i, j):
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            neighbors = []
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                    neighbors.append((ni, nj))
            return neighbors

        def search(pos, curr_word):
            curr_word = curr_word + board[pos[0]][pos[1]]
            
            if curr_word != word[:len(curr_word)]:
                return False
            if len(curr_word) == len(word):
                return True
                
            for nb in get_valid_neighbors(pos[0], pos[1]):
                if nb not in visiting:
                    visiting.add(nb)
                    if search(nb, curr_word):
                        return True
                    visiting.remove(nb) 
            
        for i in range(len(board)):
            for j, char in enumerate(board[i]):
                if char == word[0]:
                    visiting.add((i, j))
                    if search((i, j), ''):
                        return True
                    visiting.remove((i, j))
        
        return False