def wordSearch(board, word):
    rows, cols = len(board), len(board[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    def dfs(r, c, index):
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
            return False
        temp, board[r][c] = board[r][c], '/'
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if dfs(nr, nc, index+1):
                return True
        board[r][c] = temp
        return False

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

class Solution:
    def wordSearch(self, board: List[List[str]], word: str) -> bool:
        return wordSearch(board, word)

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.wordSearch([["A", "B", "C"], ["D", "E", "F"]], "BFEE"))  # Expected: True
    print(s.wordSearch([["A", "B", "C"], ["D", "E", "F"]], "ABCF"))  # Expected: False