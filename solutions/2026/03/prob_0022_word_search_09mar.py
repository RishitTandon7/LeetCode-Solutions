from typing import List, Optional

class Solution:
    def wordSearch(self, board: List[List[str]], word: str) -> bool:
        """
        Approach: 
        Time Complexity: O(m*n*len(word))
        Space Complexity: O(1)
        """
        # Define the directions for DFS
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Function to check if a cell is within the board and contains the character
        def isValid(x, y):
            return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == word[i]
        
        # Function to perform DFS
        def dfs(x, y, i):
            # If the current character is not in the word, return False
            if not isValid(x, y):
                return False
            # If the current character is the last character in the word, return True
            if i == len(word) - 1:
                return True
            # Mark the current cell as visited
            temp = board[x][y]
            board[x][y] = '#'
            # Perform DFS in all directions
            for dx, dy in directions:
                if dfs(x + dx, y + dy, i + 1):
                    return True
            # Unmark the current cell
            board[x][y] = temp
            return False
        
        # Iterate over each cell in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                # If the current cell contains the first character of the word, perform DFS
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        # If the word is not found, return False
        return False

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.wordSearch([["A","B","C","E"],["S","F","C","E"],["A","D","E","D"],["S","B","C","E"]], "ABCCED"))  # Expected: True
    print(s.wordSearch([["A","B","C","E"],["S","F","C","E"],["A","D","E","D"],["S","B","C","E"]], "SEE"))  # Expected: True
    print(s.wordSearch([["A","B","C","E"],["S","F","C","E"],["A","D","E","D"],["S","B","C","E"]], "ABCB"))  # Expected: False