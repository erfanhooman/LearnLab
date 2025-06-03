import heapq
from abc import ABC, abstractmethod
from collections import deque

from puzzle import Puzzle


class PuzzleSolver(ABC):
    """
    Abstract base class for a puzzle solver.

    Attributes:
        puzzle: An instance of Puzzle.
    """

    def __init__(self, puzzle: Puzzle):
        self.puzzle = puzzle

    @abstractmethod
    def solve(self):
        """
        Solve the puzzle using a specific search algorithm.
        """
        pass

    def get_successors(self, state):
        """
        Return a List of Possible moves and the resulting state
        """

        successors = []
        zero_index = state.index(0)  # find the empty place
        row, col = zero_index // 3, zero_index % 3

        moves = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }

        for move, (dr, dc) in moves.items():
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_state = list(state)
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                successors.append((move, tuple(new_state)))

        return successors

    def print_soloution(self, path):
        """
        Prints the solution steps.
        """
        print("Solution Path:")
        for step, move in enumerate(path, 1):
            print(f"Step {step}: {move}")


class BFSSolver(PuzzleSolver):
    """
    Solves the 8-puzzle using Breadth-First Search (BFS).
    """

    def __init__(self, puzzle: Puzzle):
        super().__init__(puzzle)

    def solve(self):
        initial_state = tuple(self.puzzle.initial_state)
        goal_state = tuple(self.puzzle.goal_state)

        queue = deque([(initial_state, [])])

        visited = set()

        while queue:
            current_state, path = queue.popleft()

            if current_state == goal_state:
                print("Solution found!")
                self.print_soloution(path)
                return path

            if current_state in visited:
                continue
            visited.add(current_state)

            print(Puzzle(current_state))

            for move, new_state in self.get_successors(current_state):
                if new_state not in visited:
                    new_path = path + [move]
                    queue.append((new_state, new_path))

        print("No solution found.")
        return None


class DFSSolver(PuzzleSolver):
    """
    Solves the 8-puzzle using Depth-First Search (DFS).
    """

    def __init__(self, puzzle: Puzzle):
        super().__init__(puzzle)

    def solve(self):
        initial_state = tuple(self.puzzle.initial_state)
        goal_state = tuple(self.puzzle.goal_state)

        stack = [(initial_state, [])]

        visited = set()

        while stack:
            current_state, path = stack.pop()

            if current_state == goal_state:
                print("Solution found!")
                self.print_soloution(path)
                return path

            if current_state in visited:
                continue
            visited.add(current_state)

            print(Puzzle(current_state))

            for move, new_state in self.get_successors(current_state):
                if new_state not in visited:
                    new_path = path + [move]
                    stack.append((new_state, new_path))

        print("No solution found.")
        return None


class AStarSolver(PuzzleSolver):
    """
    Solves the 8-puzzle using A* Search with Manhattan distance heuristic.
    """

    def __init__(self, puzzle: Puzzle):
        super().__init__(puzzle)

    def solve(self):
        initial_state = tuple(self.puzzle.initial_state)
        goal_state = tuple(self.puzzle.goal_state)

        """
        we are going to store (priority, current_state, path_so_far) in a minheap
        use heap so node with lower f(n) expand first
        """
        frontier = []
        heapq.heappush(frontier, (0, initial_state, []))

        """
        explored set to avoid revisiting state
        """
        explored = set()

        while frontier:
            """
            expand the node with lowest f(n) from min-heap
            """
            cost, current_state, path = heapq.heappop(frontier)

            if current_state == goal_state:
                print("Solved")
                self.print_soloution(path)
                return path

            if current_state in explored:
                continue
            explored.add(current_state)

            print(Puzzle(current_state))

            """
            find all of the possible moves from here
            """
            for move, new_state in self.get_successors(current_state):
                """
                the A* algorithm priority calculate by:
                    g(n): len(new_path) -> the number of moves so far
                    +
                    h(n): self.manhattan(new_state, goal_state) -> manhattan distance
                """
                if new_state not in explored:
                    new_path = path + [move]
                    priority = len(new_path) + self.manhattan_distance(new_state, goal_state)

                    """
                    push the new node into the frontier with the calculated priority and the new state and new path
                    """
                    heapq.heappush(frontier, (priority, new_state, new_path))

        print("No Solution Found")
        return None

    def manhattan_distance(self, state, goal_state):
        """
        Computes the Manhattan distance heuristic.
        Manhattan distance = sum of |x1 - x2| + |y1 - y2| for each tile
        """
        distance = 0
        for i in range(1, 9):
            x1, y1 = self.get_position(state, i)
            x2, y2 = self.get_position(goal_state, i)
            distance += (x1 - x2) ** 2 + (y1 - y2) ** 2
        return distance

    def get_position(self, state, value):
        """
        Returns the (row, col) position of a tile in a 3x3 grid.
        """
        index = state.index(value)
        return index // 3, index % 3
