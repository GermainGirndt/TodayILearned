import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd


STATE_VALUE = {
    "START": "A",
    "FINISH": "F",
    "WALL": "X",
    "EMPTY": " "
}


class Action:
    def __init__(self, name):
        self.name = name
        self.row_change = 0
        self.column_change = 0

        if name == "UP":
            self.row_change = -1
            self.column_change = 0
        elif name == "DOWN":
            self.row_change = 1
            self.column_change = 0
        elif name == "LEFT":
            self.row_change = 0
            self.column_change = -1
        elif name == "RIGHT":
            self.row_change = 0
            self.column_change = 1
        else:
            raise Exception("Invalid action name")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def apply(self, position):
        row = position.row + self.row_change
        column = position.column + self.column_change

        return Position(row, column)


class Position:

    def __init__(self, row, column):
        self.row = row
        self.column = column


class State:
    def __init__(self, state_number, value, row, column):
        self.state_number = state_number
        self.value = value
        self.row = row
        self.column = column

    def __str__(self):
        return str(self.state_number)

    def __repr__(self):
        return str(self.state_number)

    @staticmethod
    def is_value_valid(value):
        return value in list(STATE_VALUE.values())

    def __hash__(self):
        return self.state_number


class Maze:

    def __init__(self, maze_array):
        self.maze_array = maze_array

        self.POSSIBLE_ACTIONS = [Action("UP"), Action(
            "DOWN"), Action("LEFT"), Action("RIGHT")]
        self.NUMBER_ROWS = len(self.maze_array)
        self.NUMBER_COLUMNS = len(self.maze_array[0])
        self.NUMBER_STATES = self.NUMBER_ROWS * self.NUMBER_COLUMNS
        self.NUMBER_ACTIONS = len(self.POSSIBLE_ACTIONS)

        for row_index, row in enumerate(self.maze_array):
            for column_index, column in enumerate(row):
                state_value = self.maze_array[row_index][column_index]
                state = State(self.calculate_state_number(
                    row_index, column_index), state_value, row_index, column_index)
                self.maze_array[row_index][column_index] = state

    def find_state(self, searched_state_value):
        for row_index, row in enumerate(self.maze_array):
            for column_index, column in enumerate(row):
                state = self.maze_array[row_index][column_index]
                if state.value == searched_state_value:
                    return state
        raise Exception("State not found")

    def calculate_state_number(self, state_row, state_column):
        return self.NUMBER_COLUMNS * state_row + state_column

    def get_state_at(self, position):
        return self.maze_array[position.row][position.column]

    def apply_action_to_state(self, action, state):
        position = Position(state.row, state.column)
        position_candidate = action.apply(position)
        if self.is_valid_position(position_candidate):
            return self.get_state_at(position_candidate)
        else:
            return state

    def is_valid_position(self, position):
        state = self.get_state_at(position)
        return self.is_valid_state(state)

    def is_valid_state(self, state):
        return state.value != STATE_VALUE["WALL"]

    def calculate_trasition_functions(self):
        transition_functions = np.zeros(
            (maze.NUMBER_STATES, maze.NUMBER_ACTIONS, maze.NUMBER_STATES))

        agent_start_state = maze.find_state(STATE_VALUE["START"])
        states_to_visit_queue = [agent_start_state]

        visited_states = {}
        while states_to_visit_queue:
            state = states_to_visit_queue.pop(0)

            if visited_states.get(state.state_number):
                continue

            for action_index, action in enumerate(maze.POSSIBLE_ACTIONS):
                state_prime = maze.apply_action_to_state(action, state)
                transition_functions[state.state_number,
                                     action_index, state_prime.state_number] = 1
                states_to_visit_queue.append(state_prime)

            visited_states[state.state_number] = True
        return transition_functions

    def get_reward_function(self):
        reward_function = np.zeros(
            (maze.NUMBER_STATES, maze.NUMBER_ACTIONS, maze.NUMBER_STATES))
        end_state = maze.find_state(STATE_VALUE["FINISH"])
        # setting the reward only for reaching the end state
        reward_function[:, :, end_state.state_number] = 1
        return reward_function

    def learn_best_way_out(self):

        epsilon = 0.7  # dont set this to close to 9 otherwise it wont learn.
        gamma = 0.9  # discount factor
        alfa = 0.1  # learning rate
        max_runs = 100  # the max nr of episodes from start to end state
        # we assume all gridworlds have 4 actions
        nr_of_actions = len(maze.POSSIBLE_ACTIONS)
        queue_table_rewards = np.zeros((maze.NUMBER_STATES, nr_of_actions))

        reward_function = maze.get_reward_function()

        logger = Logger(queue_table_rewards)
        for i in range(1, max_runs):

            agent_start_state = maze.find_state(STATE_VALUE["START"])
            s = agent_start_state.state_number
            end_state = maze.find_state(STATE_VALUE["FINISH"])

            while s != end_state.state_number:

                a = np.random.randint(0, nr_of_actions) if np.random.random(
                ) > epsilon else np.argmax(queue_table_rewards[s])

                print(a)
                print(transition_functions[s, a])

                s_prime = random.choices(
                    np.arange(0, maze.NUMBER_STATES), weights=transition_functions[s, a], k=1)[0]

                td = (reward_function[s, a, s_prime]+gamma*np.max(
                    queue_table_rewards[s_prime])-queue_table_rewards[s, a])

                queue_table_rewards[s, a] = queue_table_rewards[s, a]+alfa*td

                s = s_prime

                logger.tick()  # just for logging the steps to get to the terminal_state so you can plot the learing curve
            logger.log()  # just to tell the logger class that an episode (run) has ended
        logger.show()  # just to tell the logger to plot and print the output for you


class Logger:
    def __init__(self, queue_table_rewards):
        self.queue_table_rewards = queue_table_rewards
        self.data = []
        self.step = 0

    def log(self):
        self.data.append(self.step)
        self.step = 0

    def tick(self):
        self.step = self.step+1

    def show(self):
        plt.plot(self.data)
        print(self.queue_table_rewards)
        plt.show()


def write_array_to_file(array, filename, title):
    with open(filename, 'a') as file:
        file.write(f"{title}\n")
        for item in array:
            file.write(str(item) + '\n')

        file.write("\n")
        for state_index, actions in enumerate(array):
            file.write(f"State Index - {state_index}:\n")
            for action_index, action in enumerate(actions):
                file.write(
                    f"Action Index - {action_index} ({maze.POSSIBLE_ACTIONS[action_index]}):\n")
                file.write(f"{str(action)}\n")
            file.write('\n')

######################################################

# 1. Parse the maze into a 2D array


FILE_NAME = "test_maze_2.txt"
maze_array = []

with open(FILE_NAME, "r") as file:
    # I need to break the file into lines, so that I can append each line as a row in my 2D array maze
    lines = file.readlines()
    for line in lines:
        row = []
        for character in line:
            if State.is_value_valid(character):
                row.append(character)
        maze_array.append(row)


# 2. Construct the Transition Matrix
maze = Maze(maze_array)
transition_functions = maze.calculate_trasition_functions()
write_array_to_file(transition_functions, "output.txt",
                    "--- Transition Functions")


# 3. Construct the Reward Matrix

reward_function = maze.get_reward_function()
write_array_to_file(reward_function, "output.txt",
                    "--- Reward Function before training")
maze.learn_best_way_out()
