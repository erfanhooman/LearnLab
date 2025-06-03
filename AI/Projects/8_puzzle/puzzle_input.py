import random
import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

from puzzle import Puzzle


class PuzzleInputStrategy(ABC):
    """
    Abstract base class for different ways to obtain a puzzle.
    """
    @abstractmethod
    def get_puzzle(self) -> Puzzle:
        raise NotImplemented


class UserInputStrategy(PuzzleInputStrategy):
    """
    Gets puzzle input from the user via mouse and keyboard.
    """
    def get_puzzle(self):
        def submit():
            nonlocal initial_state
            try:
                input_values = [int(entry.get()) for entry in entries]
                if len(input_values) != 9 or sorted(input_values) != list(range(9)):
                    raise ValueError("Invalid input: Must contain digits 0-8 exactly once.")
                initial_state = input_values
                root.quit()
            except ValueError as e:
                messagebox.showerror("Input Error", str(e))

        root = tk.Tk()
        root.title("Enter Puzzle State")

        entries = []
        for i in range(3):
            for j in range(3):
                entry = tk.Entry(root, width=5, font=("Arial", 18))
                entry.grid(row=i, column=j)
                entries.append(entry)

        submit_button = tk.Button(root, text="Submit", command=submit)
        submit_button.grid(row=3, column=0, columnspan=3)

        initial_state = []
        root.mainloop()
        root.destroy()

        return Puzzle(initial_state)


class RandomPuzzleStrategy(PuzzleInputStrategy):
    """
    Generates a random 8-puzzle configuration.
    """
    def get_puzzle(self):
        num_moves = int(input("Enter the number of random moves: "))
        initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

        for _ in range(num_moves):
            zero_index = initial_state.index(0)
            neighbors = []

            if zero_index % 3 != 0:  # can move left
                neighbors.append(zero_index - 1)
            if zero_index % 3 != 2:  # can move right
                neighbors.append(zero_index + 1)
            if zero_index > 2:  # can move up
                neighbors.append(zero_index - 3)
            if zero_index < 6:  # can move down
                neighbors.append(zero_index + 3)

            swap_with = random.choice(neighbors)
            initial_state[zero_index], initial_state[swap_with] = initial_state[swap_with], initial_state[zero_index]

        return Puzzle(initial_state)


class FilePuzzleStrategy(PuzzleInputStrategy):
    """
    Reads the puzzle configuration from a file.
    """

    def get_puzzle(self):
        while True:
            file_path = input("Enter the file path: ")
            try:
                with open(file_path, 'r') as file:
                    lines = [line.strip() for line in file.readlines()]
                    if len(lines) != 3:
                        raise ValueError("Invalid file format: Must have exactly 3 rows.")

                    initial_state = []
                    for line in lines:
                        numbers = list(map(int, line.split()))
                        if len(numbers) != 3:
                            raise ValueError("Invalid file format: Each row must contain exactly 3 numbers.")

                        initial_state.extend(numbers)

                    if sorted(initial_state) != list(range(9)):
                        raise ValueError("Invalid file content: Must contain numbers 0-8 exactly once.")

                    return Puzzle(initial_state)

            except Exception as e:
                print(f"Error: {e}")
                print("Please try again with a valid file.")
