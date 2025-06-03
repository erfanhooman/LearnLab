
# Puzzle Representation

class Puzzle:
    """
    Represents an 8-puzzle state.

    Attributes:
        initial_state: The starting configuration.
        goal_state: The target configuration.
    """

    def __init__(self, initial_state, goal_state=[1, 2, 3, 4, 5, 6, 7, 8, 0]):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def __str__(self):
        row1 = self.initial_state[0:3]
        row2 = self.initial_state[3:6]
        row3 = self.initial_state[6:9]

        result = (
            '--------' + '\n' +
            ''.join(map(str, row1)) + '\n' +
            ''.join(map(str, row2)) + '\n' +
            ''.join(map(str, row3)) + '\n' +
            '--------'
        )
        return result