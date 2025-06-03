from puzzle_input import (PuzzleInputStrategy,
                          UserInputStrategy,
                          RandomPuzzleStrategy,
                          FilePuzzleStrategy)

from puzzle_solver import (PuzzleSolver,
                           BFSSolver,
                           DFSSolver,
                           AStarSolver)

from puzzle import Puzzle
import time
import psutil

def track_performance(solver: PuzzleSolver):
    """
    Tracks execution time and memory usage.
    """
    process = psutil.Process()

    mem_before = process.memory_info().rss
    start_time = time.time()

    solution = solver.solve()

    end_time = time.time()
    mem_after = process.memory_info().rss

    print("\n--- Performance Metrics ---")
    print(f"Time Taken: {end_time - start_time:.4f} seconds")
    print(f"Memory Usage: {mem_after - mem_before:.4f}")

    return solution


def select_input_strategy(choice: int) -> PuzzleInputStrategy:
    """
    Returns the corresponding PuzzleInputStrategy based on user choice.
    """
    if choice == 1:
        return UserInputStrategy()
    elif choice == 2:
        return RandomPuzzleStrategy()
    elif choice == 3:
        return FilePuzzleStrategy()
    else:
        raise ValueError("Invalid puzzle input method choice.")


def select_solver(puzzle: Puzzle, choice: int) -> PuzzleSolver:
    """
    Returns the corresponding PuzzleSolver based on user choice.
    """
    if choice == 1:
        return BFSSolver(puzzle)
    elif choice == 2:
        return DFSSolver(puzzle)
    elif choice == 3:
        return AStarSolver(puzzle)
    else:
        raise ValueError("Invalid solver method choice.")


def main():
    print("Select Puzzle Input Method:")
    print("1 - User Input")
    print("2 - Random Puzzle")
    print("3 - File Input")
    input_choice = int(input("Enter your choice: "))

    input_strategy = select_input_strategy(input_choice)
    puzzle = input_strategy.get_puzzle()

    if not puzzle:
        puzzle = Puzzle(initial_state=[1, 2, 3, 4, 5, 6, 7, 8, 0],
                        goal_state=[1, 2, 3, 4, 5, 6, 7, 8, 0])

    print("\nPuzzle Selected:")
    print(puzzle)

    print("\nSelect Solver Method:")
    print("1 - Uniformed Search (BFS)")
    print("2 - Uniformed Search (DFS)")
    print("3 - Informed Search (A* Search)")
    solver_choice = int(input("Enter your choice: "))

    solver = select_solver(puzzle, solver_choice)

    print("\nSolving the puzzle using your selected method...")
    track_performance(solver)


if __name__ == "__main__":
    main()
