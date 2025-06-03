from abc import ABC, abstractmethod
from typing import List, Tuple, Optional, Dict, Set
import random
import copy

from board import SudokuBoard

class SudokuSolver(ABC):
    """Abstract base class for different solving strategies"""

    def __init__(self, board: SudokuBoard):
        self.board = board
        self.steps = 0
        self.backtracks = 0

    @abstractmethod
    def solve(self) -> Tuple[bool, SudokuBoard]:
        """Solve the sudoku puzzle"""
        pass

    def get_statistics(self) -> dict:
        """Return solving statistics"""
        return {
            'steps': self.steps,
            'backtracks': self.backtracks
        }


class BacktrackingSolver(SudokuSolver):
    def solve(self) -> Tuple[bool, SudokuBoard]:
        board_copy = self.board.copy()
        success = self._backtrack(board_copy)
        return success, board_copy

    def _backtrack(self, board: SudokuBoard) -> bool:
        self.steps += 1
        empty_cells = board.get_empty_cells()

        if not empty_cells:
            return True  # Solved

        row, col = empty_cells[0]

        for num in range(1, 10):
            if board.is_valid_move(row, col, num):
                board.board[row][col] = num
                board.display()  # Show progress
                print(f"Trying {num} at ({row}, {col})\n")

                if self._backtrack(board):
                    return True

                board.board[row][col] = 0
                self.backtracks += 1

        return False


class ForwardCheckingSolver(SudokuSolver):
    def solve(self) -> Tuple[bool, SudokuBoard]:
        board_copy = self.board.copy()
        domains = self._initialize_domains(board_copy)

        def forward_check(board: SudokuBoard, domains: Dict[Tuple[int, int], Set[int]]) -> bool:
            self.steps += 1
            if board.is_complete():
                return True

            # Pick cell with smallest domain (MRV heuristic)
            row, col = min(domains, key=lambda k: len(domains[k]))

            for value in domains[(row, col)].copy():
                if board.is_valid_move(row, col, value):
                    board.board[row][col] = value
                    print(f"Step {self.steps}: Trying {value} at ({row}, {col})")
                    board.display()

                    # Forward check: reduce domains of neighbors
                    removed = self._forward_reduce(domains, row, col, value)

                    # Check for empty domains
                    if all(domains[c] for c in domains):
                        if forward_check(board, domains):
                            return True

                    # Backtrack
                    board.board[row][col] = 0
                    self.backtracks += 1
                    print(f"Backtrack {self.backtracks}: Removed {value} at ({row}, {col})")
                    board.display()
                    self._restore_domains(domains, removed)

            return False

        success = forward_check(board_copy, domains)
        return success, board_copy if success else None

    def _initialize_domains(self, board: SudokuBoard) -> Dict[Tuple[int, int], Set[int]]:
        domains = {}
        for row in range(9):
            for col in range(9):
                if board.board[row][col] == 0:
                    domains[(row, col)] = board.get_possible_values(row, col)
        return domains

    def _forward_reduce(self, domains: Dict[Tuple[int, int], Set[int]],
                        row: int, col: int, value: int) -> Dict[Tuple[int, int], Set[int]]:
        removed = {}
        for r, c in domains:
            if (r == row or c == col or (r // 3, c // 3) == (row // 3, col // 3)) and (r, c) != (row, col):
                if value in domains[(r, c)]:
                    domains[(r, c)].remove(value)
                    removed.setdefault((r, c), set()).add(value)
        del domains[(row, col)]  # remove assigned variable
        return removed

    def _restore_domains(self, domains: Dict[Tuple[int, int], Set[int]],
                         removed: Dict[Tuple[int, int], Set[int]]) -> None:
        for cell, values in removed.items():
            if cell in domains:
                domains[cell].update(values)
            else:
                domains[cell] = set(values)


class MinConflictsSolver(SudokuSolver):
    def __init__(self, board: SudokuBoard, max_steps: int = 10000):
        super().__init__(board)
        self.max_steps = max_steps

    def solve(self) -> Tuple[bool, SudokuBoard]:
        board_copy = self._initialize_complete_board(self.board.copy())

        for step in range(self.max_steps):
            self.steps += 1
            conflicted = self._get_conflicted_cells(board_copy)
            if not conflicted:
                return True, board_copy

            row, col = random.choice(conflicted)
            min_conflict_value = self._min_conflict_value(board_copy, row, col)
            board_copy.board[row][col] = min_conflict_value

            if step % 100 == 0:
                print(f"Step {step}: resolving conflicts...")
                board_copy.display()

        return False, None

    def _initialize_complete_board(self, board: SudokuBoard) -> SudokuBoard:
        """Fill empty cells randomly per 3x3 box without duplicates"""
        for box_row in range(3):
            for box_col in range(3):
                used = set()
                empty = []
                for r in range(box_row * 3, (box_row + 1) * 3):
                    for c in range(box_col * 3, (box_col + 1) * 3):
                        val = board.board[r][c]
                        if val != 0:
                            used.add(val)
                        else:
                            empty.append((r, c))
                candidates = list(set(range(1, 10)) - used)
                random.shuffle(candidates)
                for (r, c), val in zip(empty, candidates):
                    board.board[r][c] = val
        return board

    def _get_conflicted_cells(self, board: SudokuBoard) -> List[Tuple[int, int]]:
        conflicted = []
        for row in range(9):
            for col in range(9):
                if self._count_conflicts(board, row, col, board.board[row][col]) > 0:
                    conflicted.append((row, col))
        return conflicted

    def _min_conflict_value(self, board: SudokuBoard, row: int, col: int) -> int:
        min_conflicts = float('inf')
        best_value = board.board[row][col]

        for val in range(1, 10):
            if val != board.board[row][col]:
                conflicts = self._count_conflicts(board, row, col, val)
                if conflicts < min_conflicts:
                    min_conflicts = conflicts
                    best_value = val

        return best_value

    def _count_conflicts(self, board: SudokuBoard, row: int, col: int, value: int) -> int:
        count = 0
        for i in range(9):
            if i != col and board.board[row][i] == value:
                count += 1
            if i != row and board.board[i][col] == value:
                count += 1

        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if (i, j) != (row, col) and board.board[i][j] == value:
                    count += 1
        return count