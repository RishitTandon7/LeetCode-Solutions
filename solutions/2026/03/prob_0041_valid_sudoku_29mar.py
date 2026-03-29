from typing import List, Optional

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                num = int(val)
                box_index = (i // 3) * 3 + j // 3

                # Check row and column
                if num - 1 in rows[i] or num - 1 in cols[j]:
                    return False

                # Check box
                if num - 1 in boxes[box_index]:
                    return False

                # Add to sets
                rows[i].add(num - 1)
                cols[j].add(num - 1)
                boxes[box_index].add(num - 1)

        return True