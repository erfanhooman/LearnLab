from typing import List, Tuple, Set, Optional

from input import SudokuInputStrategy, ManualInputStrategy, PredefinedSudokuStrategy, FileInputStrategy
from solver import SudokuSolver, BacktrackingSolver, ForwardCheckingSolver, MinConflictsSolver
from board import SudokuBoard

class SudokuSolverFactory:
    """Factory for creating different solver instances"""

    @staticmethod
    def create_solver(solver_type: str, board: SudokuBoard, **kwargs) -> SudokuSolver:
        """Create solver instance based on type"""
        solvers = {
            'backtracking': BacktrackingSolver,
            'forward_checking': ForwardCheckingSolver,
            'min_conflicts': MinConflictsSolver
        }

        if solver_type not in solvers:
            raise ValueError(f"Unknown solver type: {solver_type}")

        if solver_type == 'min_conflicts':
            max_steps = kwargs.get('max_steps', 1000)
            return solvers[solver_type](board, max_steps)
        else:
            return solvers[solver_type](board)

class SudokuInputFactory:
    """Factory for creating different input strategy instances"""

    @staticmethod
    def create_input_strategy(input_type: str, **kwargs) -> SudokuInputStrategy:
        """Create input strategy instance based on type"""
        strategies = {
            'manual': ManualInputStrategy,
            'predefined': PredefinedSudokuStrategy,
            'file': FileInputStrategy
        }

        if input_type not in strategies:
            raise ValueError(f"Unknown input type: {input_type}")

        if input_type == 'file':
            filename = kwargs.get('filename', 'sudoku.txt')
            return strategies[input_type](filename)
        else:
            return strategies[input_type]()


class SudokuCSPSolver:
    """Main class that orchestrates the solving process"""

    def __init__(self):
        self.board = None
        self.solver = None

    def get_sudoku_input(self, input_type: str, **kwargs) -> None:
        """Get sudoku input using specified strategy"""
        input_strategy = SudokuInputFactory.create_input_strategy(input_type, **kwargs)
        self.board = input_strategy.get_sudoku()

    def solve_sudoku(self, solver_type: str, **kwargs) -> Tuple[bool, Optional[SudokuBoard], dict]:
        """Solve sudoku using specified algorithm"""
        if self.board is None:
            raise ValueError("No sudoku board loaded. Please get input first.")

        self.solver = SudokuSolverFactory.create_solver(solver_type, self.board, **kwargs)
        success, solution = self.solver.solve()
        statistics = self.solver.get_statistics()

        return success, solution, statistics

    def run_interactive_session(self) -> None:
        """Run interactive session for solving sudoku"""
        pass


def main():
    """Main function demonstrating usage"""
    solver = SudokuCSPSolver()

    print("Sudoku CSP Solver")
    print("================")

    while True:
        input_strategy = input("enter your input strategy between 'manual', 'predefined' and 'file': ")
        if input_strategy not in ('manual', 'predefined', 'file'):
            print("Unknown solver type")
        else:
            break

    solver.get_sudoku_input(input_strategy)

    while True:
        solver_strategy = input("enter your solver strategy between 'backtracking', 'forward_checking' and 'min_conflicts': ")
        if solver_strategy not in ('backtracking', 'forward_checking', 'min_conflicts'):
            print("Unknown solver type")
        else:
            break

    success, solution, stats = solver.solve_sudoku(solver_strategy)

    if solution is None:
        print("No solution found")
        return

    solution.display()


if __name__ == "__main__":
    main()