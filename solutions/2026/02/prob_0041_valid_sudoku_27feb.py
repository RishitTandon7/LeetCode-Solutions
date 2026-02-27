from typing import List, Optional

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Approach: We use two sets to track the numbers in each row and column.
        Time Complexity: O(81) because we iterate over each cell in the board.
        Space Complexity: O(81) because we store the numbers in sets.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue

                box_index = (i // 3) * 3 + j // 3
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        return True

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                           ["6",".",".","1","9","5",".",".","."],
                           [".","9","8",".",".",".",".","6","."],
                           ["8",".",".",".","6",".",".",".","3"],
                           ["4",".",".","8",".","3",".",".","1"],
                           ["7",".",".",".","2",".",".",".","6"],
                           [".","6",".",".",".",".","2","8","."],
                           [".",".",".","4","1","9",".",".","5"],
                           [".",".",".",".","8",".",".","7","9"]]))  # Expected: True

    print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."],
                           ["6",".",".","1","9","5",".",".","."],
                           [".","9","8",".",".",".",".","6","."],
                           ["8",".",".",".","6",".",".",".","3"],
                           ["4",".",".","8",".","3",".",".","1"],
                           ["7",".",".",".","2",".",".",".","6"],
                           [".","6",".",".",".",".","2","8","."],
                           [".",".",".","4","1","9",".",".","5"],
                           [".",".",".",".","8",".",".","7","9"]]))  # Expected: False