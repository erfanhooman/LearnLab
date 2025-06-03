from typing import List, Tuple, Set
import copy


class SudokuBoard:
    """Represents a Sudoku board with utility methods"""

    def __init__(self, board: List[List[int]] = None):
        if board is None:
            self.board = [[0 for _ in range(9)] for _ in range(9)]
        else:
            self.board = copy.deepcopy(board)

    def is_valid_move(self, row: int, col: int, num: int) -> bool:
        # Check row and column
        if any(self.board[row][c] == num for c in range(9)):
            return False
        if any(self.board[r][col] == num for r in range(9)):
            return False

        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if self.board[r][c] == num:
                    return False
        return True

    def get_empty_cells(self) -> List[Tuple[int, int]]:
        return [(r, c) for r in range(9) for c in range(9) if self.board[r][c] == 0]

    def get_possible_values(self, row: int, col: int) -> Set[int]:
        if self.board[row][col] != 0:
            return set()

        possible = set(range(1, 10))
        used = {self.board[row][c] for c in range(9)} | \
               {self.board[r][col] for r in range(9)} | \
               {self.board[r][c]
                for r in range((row // 3) * 3, (row // 3) * 3 + 3)
                for c in range((col // 3) * 3, (col // 3) * 3 + 3)}
        return possible - used

    def is_complete(self) -> bool:
        return all(self.board[r][c] != 0 for r in range(9) for c in range(9))

    def is_valid(self) -> bool:
        for r in range(9):
            row = [num for num in self.board[r] if num != 0]
            if len(row) != len(set(row)):
                return False

        for c in range(9):
            col = [self.board[r][c] for r in range(9) if self.board[r][c] != 0]
            if len(col) != len(set(col)):
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = [
                    self.board[r][c]
                    for r in range(box_row, box_row + 3)
                    for c in range(box_col, box_col + 3)
                    if self.board[r][c] != 0
                ]
                if len(box) != len(set(box)):
                    return False

        return True

    def display(self) -> None:
        for i, row in enumerate(self.board):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j, val in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(val if val != 0 else ".", end=" ")
            print()
        print()

    def copy(self) -> 'SudokuBoard':
        """Create a deep copy of the board"""
        return SudokuBoard(self.board)
