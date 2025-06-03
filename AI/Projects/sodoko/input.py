from abc import ABC, abstractmethod
import os
from typing import List

from board import SudokuBoard


class SudokuInputStrategy(ABC):
    """Abstract strategy for different input methods"""

    @abstractmethod
    def get_sudoku(self) -> SudokuBoard:
        """Get a sudoku board using specific input method"""
        pass


class ManualInputStrategy(SudokuInputStrategy):
    """Strategy for manual cell-by-cell input with beautiful UI"""

    def get_sudoku(self) -> SudokuBoard:
        """Get sudoku by manual input with interactive cell-by-cell interface"""
        import os

        board = [[0 for _ in range(9)] for _ in range(9)]
        current_row, current_col = 0, 0

        while True:
            try:
                # Clear screen for better UX (works on most terminals)
                if os.name == 'nt':  # Windows
                    os.system('cls')
                else:  # Unix/Linux/Mac
                    os.system('clear')

                # Display the Sudoku grid
                self._display_sudoku_grid(board, current_row, current_col)

                # Show current position info
                box_num = (current_row // 3) * 3 + (current_col // 3) + 1
                print(f"\n📍 Current Position: Row {current_row + 1}, Column {current_col + 1} (Box {box_num})")

                # Show completion progress
                filled_cells = sum(1 for i in range(9) for j in range(9) if board[i][j] != 0)
                progress = (filled_cells / 81) * 100
                progress_bar = "█" * int(progress // 5) + "░" * (20 - int(progress // 5))
                print(f"📊 Progress: [{progress_bar}] {filled_cells}/81 cells ({progress:.1f}%)")

                # Get user input
                user_input = input(
                    f"\n🎯 Enter value for cell [{current_row + 1},{current_col + 1}] (0 for empty): ").strip().lower()

                if user_input == 'quit':
                    print("\n❌ Input cancelled by user.")
                    return SudokuBoard()
                elif user_input == 'reset':
                    confirm = input("⚠️  Are you sure you want to clear the entire board? (y/n): ").strip().lower()
                    if confirm in ['y', 'yes']:
                        board = [[0 for _ in range(9)] for _ in range(9)]
                        current_row, current_col = 0, 0
                        print("✅ Board cleared!")
                    continue
                elif user_input == 'back':
                    if current_row == 0 and current_col == 0:
                        print("⚠️  Already at the first cell!")
                        input("Press ENTER to continue...")
                        continue
                    current_col -= 1
                    if current_col < 0:
                        current_col = 8
                        current_row -= 1
                    continue

                # Handle number input
                if user_input == '' or user_input == '0':
                    board[current_row][current_col] = 0
                    print("✅ Cell cleared!")
                else:
                    try:
                        value = int(user_input)
                        if 1 <= value <= 9:
                            board[current_row][current_col] = value
                            print(f"✅ Set cell to {value}!")
                        else:
                            print("❌ Please enter a number between 1-9!")
                            input("Press ENTER to continue...")
                            continue
                    except ValueError:
                        print("❌ Invalid input! Please enter a number, or use commands.")
                        input("Press ENTER to continue...")
                        continue

                # Move to next cell
                current_col += 1
                if current_col > 8:
                    current_col = 0
                    current_row += 1

                # Check if we've completed the board
                if current_row > 8:
                    # Clear screen and show final board
                    if os.name == 'nt':
                        os.system('cls')
                    else:
                        os.system('clear')

                    self._display_final_sudoku_grid(board)

                    while True:
                        confirm = input("\n✨ Is this Sudoku puzzle correct? (y/n/edit): ").strip().lower()
                        if confirm in ['y', 'yes']:
                            print("🎊 Excellent! Board accepted!")
                            return SudokuBoard(board)
                        elif confirm in ['n', 'no']:
                            print("🔄 Let's start over...")
                            return self.get_sudoku()
                        elif confirm == 'edit':
                            current_row, current_col = 0, 0
                            break
                        else:
                            print("Please enter 'y' for yes, 'n' for no, or 'edit' to modify.")

                    if confirm == 'edit':
                        continue

            except KeyboardInterrupt:
                print("\n\n❌ Input cancelled by user.")
                return SudokuBoard()
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                input("Press ENTER to continue...")
                continue

    def _display_sudoku_grid(self, board: List[List[int]], highlight_row: int = -1, highlight_col: int = -1) -> None:
        """Display a beautiful Sudoku grid with highlighting"""
        print("\n    " + "   ".join([f" {i + 1} " for i in range(9)]))
        print("  ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")

        for i in range(9):
            # Row separator
            if i == 3 or i == 6:
                print("  ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")
            elif i > 0:
                print("  ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")

            # Row content
            row_str = f"{i + 1} ║"
            for j in range(9):
                # Column separators
                if j == 3 or j == 6:
                    if j > 0:
                        row_str += "║"
                elif j > 0:
                    row_str += "│"

                # Cell content with highlighting
                cell_value = board[i][j]
                if i == highlight_row and j == highlight_col:
                    # Highlight current cell
                    if cell_value == 0:
                        cell_str = "🎯"
                    else:
                        cell_str = f"⭐{cell_value}"
                else:
                    if cell_value == 0:
                        cell_str = " · "
                    else:
                        cell_str = f" {cell_value} "

                row_str += cell_str

            row_str += "║"
            print(row_str)

        print("  ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")

    def _display_final_sudoku_grid(self, board: List[List[int]]) -> None:
        """Display the final beautiful Sudoku grid"""
        print("\n    " + "   ".join([f" {i + 1} " for i in range(9)]))
        print("  ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")

        for i in range(9):
            # Row separator
            if i == 3 or i == 6:
                print("  ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")
            elif i > 0:
                print("  ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")

            # Row content
            row_str = f"{i + 1} ║"
            for j in range(9):
                # Column separators
                if j == 3 or j == 6:
                    if j > 0:
                        row_str += "║"
                elif j > 0:
                    row_str += "│"

                # Cell content
                cell_value = board[i][j]
                if cell_value == 0:
                    cell_str = " · "
                else:
                    cell_str = f" {cell_value} "

                row_str += cell_str

            row_str += "║"
            print(row_str)

        print("  ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")


class PredefinedSudokuStrategy(SudokuInputStrategy):
    """Strategy for selecting from predefined sudoku puzzles"""

    def __init__(self):
        self.predefined_puzzles = [
            # Easy puzzle
            {
                "name": "Puzzle 1",
                "difficulty": "Easy",
                "board": [
                    [5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]
                ]
            },
            # Medium puzzle
            {
                "name": "Puzzle 1",
                "difficulty": "Medium",
                "board": [
                    [0, 0, 0, 6, 0, 0, 4, 0, 0],
                    [7, 0, 0, 0, 0, 3, 6, 0, 0],
                    [0, 0, 0, 0, 9, 1, 0, 8, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 5, 0, 1, 8, 0, 0, 0, 3],
                    [0, 0, 0, 3, 0, 6, 0, 4, 5],
                    [0, 4, 0, 2, 0, 0, 0, 6, 0],
                    [9, 0, 3, 0, 0, 0, 0, 0, 0],
                    [0, 2, 0, 0, 0, 0, 1, 0, 0]
                ]
            },
            # Hard puzzle
            {
                "name": "Puzzle 1",
                "difficulty": "Hard",
                "board": [
                    [0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [4, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 6, 0, 2],
                    [0, 0, 0, 0, 3, 0, 0, 7, 0],
                    [5, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 8, 0, 0, 0],
                    [0, 6, 0, 2, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 5],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            }
        ]

    def get_sudoku(self) -> SudokuBoard:
        """Get sudoku from predefined puzzles"""

        # Display available puzzles
        for i, puzzle in enumerate(self.predefined_puzzles):
            print(f"{i + 1}. {puzzle['name']} ({puzzle['difficulty']})")

        while True:
            try:
                choice = input(f"\nSelect a puzzle (1-{len(self.predefined_puzzles)}): ").strip()
                puzzle_index = int(choice) - 1

                if 0 <= puzzle_index < len(self.predefined_puzzles):
                    selected_puzzle = self.predefined_puzzles[puzzle_index]
                    print(f"\n✅ Selected: {selected_puzzle['name']}")

                    # Display the selected puzzle
                    print("\nPuzzle Preview:")
                    self._display_puzzle(selected_puzzle['board'])

                    # Confirm selection
                    while True:
                        confirm = input("\nUse this puzzle? (y/n): ").strip().lower()
                        if confirm in ['y', 'yes']:
                            return SudokuBoard(selected_puzzle['board'])
                        elif confirm in ['n', 'no']:
                            break
                        else:
                            print("Please enter 'y' for yes or 'n' for no.")

                    if confirm in ['n', 'no']:
                        continue  # Go back to puzzle selection

                else:
                    print(f"Please enter a number between 1 and {len(self.predefined_puzzles)}")

            except ValueError:
                print("Please enter a valid number!")
            except KeyboardInterrupt:
                print("\n\n❌ Selection cancelled by user.")
                return SudokuBoard()

    def _display_puzzle(self, board: List[List[int]]) -> None:
        """Display a puzzle in a nice format"""
        print("\n  ┌───────┬───────┬───────┐")
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("  ├───────┼───────┼───────┤")

            row_str = "  │"
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    row_str += "│"
                cell = str(board[i][j]) if board[i][j] != 0 else "·"
                row_str += f" {cell} "
            row_str += "│"
            print(row_str)
        print("  └───────┴───────┴───────┘")


class FileInputStrategy(SudokuInputStrategy):
    """Strategy for reading sudoku from file"""

    def __init__(self, filename: str):
        self.filename = filename

    def get_sudoku(self) -> SudokuBoard:
        """Read sudoku from file"""
        try:
            if not os.path.exists(self.filename):
                print(f"File '{self.filename}' not found!")
                self._create_sample_file()
                print(f"Sample file '{self.filename}' created!")
                return SudokuBoard()

            with open(self.filename, 'r') as file:
                lines = file.readlines()

            # Clean and filter lines
            board_lines = []
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):  # Skip empty lines and comments
                    board_lines.append(line)

            if len(board_lines) < 9:
                print(f"❌ Error: File must contain at least 9 lines of data (found {len(board_lines)})")
                print("Each line should represent a row with 9 numbers (0 for empty cells)")
                return SudokuBoard()

            board = []
            for i, line in enumerate(board_lines[:9]):  # Take only first 9 lines
                try:
                    # Try different separators
                    if ',' in line:
                        values = line.split(',')
                    elif '\t' in line:
                        values = line.split('\t')
                    else:
                        values = line.split()

                    # If still not 9 values, try treating as single string of digits
                    if len(values) != 9:
                        if len(line.replace(' ', '')) == 9:
                            values = list(line.replace(' ', ''))
                        else:
                            raise ValueError(f"Row must have exactly 9 values (found {len(values)})")

                    # Convert to integers
                    row = []
                    for j, val in enumerate(values):
                        val = val.strip()
                        try:
                            num = int(val)
                            if num < 0 or num > 9:
                                raise ValueError(f"Value must be between 0-9 (found {num})")
                            row.append(num)
                        except ValueError as ve:
                            print(f"❌ Error in row {i + 1}, column {j + 1}: {ve}")
                            return SudokuBoard()

                    board.append(row)

                except Exception as e:
                    print(f"Error parsing row {i + 1}: {e}")
                    return SudokuBoard()

            print("Sudoku loaded successfully from file!")
            print("\nLoaded puzzle:")
            self._display_board(board)

            return SudokuBoard(board)

        except Exception as e:
            print(f"Error reading file: {e}")
            return SudokuBoard()

    def _create_sample_file(self) -> None:
        """Create a sample sudoku file"""
        sample_content = """# Sample Sudoku File
# Lines starting with # are comments
# Each row should contain 9 numbers (0 for empty cells)
# You can separate numbers with spaces, commas, or tabs
# Or write them without separators (like: 530070000)

5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
"""
        try:
            with open(self.filename, 'w') as file:
                file.write(sample_content)
        except Exception as e:
            print(f"❌ Error creating sample file: {e}")

    def _display_board(self, board: List[List[int]]) -> None:
        """Display board in a nice format"""
        print("\n  ┌───────┬───────┬───────┐")
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("  ├───────┼───────┼───────┤")

            row_str = "  │"
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    row_str += "│"
                cell = str(board[i][j]) if board[i][j] != 0 else "·"
                row_str += f" {cell} "
            row_str += "│"
            print(row_str)
        print("  └───────┴───────┴───────┘")