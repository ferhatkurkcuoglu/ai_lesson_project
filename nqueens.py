

import random


class NQueens:

    """ class constructor
    initializes the instance attributes N and state """

    def __init__(self, N):
        self.state = ""
        self.N = N
        self._set_state()

    """ returns a formatted string
    that represents the instance """

    def __str__(self):
        return f"{self.N}X{self.N} NQueens board is initialized with state {self.state}"

    """ Sets the instance attribute state by displaying 
    a menu to the user. The user either enters the state 
    manually or prompts the system to generate a random state.
    Check if the input state is a valid state. """

    def _set_state(self):
        print("Press 1 to select manually." "\nPress 2 to generate randomly.")
        choice = input()
        if choice == "1":
            while True:
                entered_state = input("Please enter the state manually.")
                if self._is_valid(entered_state):
                    self.state = entered_state
                    break
                else:
                    print("Invalid state! Please try again.")
        else:
            self.generate_random_state()

    """ generates and returns a valid random state """
    def generate_random_state(self):
        for i in range(self.N):
            self.state += str(random.randint(1, self.N))
        return self.state

    """ This is an internal function that takes a state as input
    and return if this is a valid state or not """

    def _is_valid(self, state):
        if len(state) != self.N or "0" in state or not state.isdigit() or any(
                char.isdigit() and int(char) > self.N for char in state):
            return False
        else:
            return True

    """ This is the primary function of this class.
    It returns the number of attacking pairs in the given state board.
    """

    def _count_attacking_pairs(self, state):
        number_of_attacking_pairs = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if self.state[i] == self.state[j] or abs(i - j) == abs(int(self.state[i]) - int(self.state[j])):
                    number_of_attacking_pairs += 1
        return number_of_attacking_pairs


problem = NQueens(7)  # create NQueens instance
print(problem)  # print the description of the problem
print(problem._count_attacking_pairs(problem.state))
