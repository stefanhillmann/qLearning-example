import random
import numpy as np


def print_map():
    print("")
    print("@@@@@@@@@@@@@@@@@@@@@@")
    print("@              @     @")
    print("@              @     @")
    print("@      0       @     @@@@    @@@@@@@@@@@@@@@@")
    print("@              @             @              @")
    print("@              @      1      @              @")
    print("@@@@@@@@@@@    @             @              @")
    print("@              @      @@@@@@@@      2       @")
    print("@              @                            @")
    print("@       4      @      3      @              @")
    print("@              @             @              @")
    print("@              @     @@@@@@@@@@@@@@@@@@@@@@@@")
    print("@                    @")
    print("@    @@@@@@@@@@@@@@@@@")


alpha = 0.1  # learning rate
gamma = 0.5  # discount factor
episodes = 500  # number of episodes

state_0 = 0
state_1 = 1
state_2 = 2
state_3 = 3
state_4 = 4
state_5 = 5

goal_state = state_5

states = [state_0, state_1, state_2, state_3, state_4, state_5]
no_states = len(states)


r_matrix = [[0, 0, 0, 0, 0, 0] for x in range(6)]
q_matrix = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0] for x in range(6)]

r_matrix[state_1][state_5] = 100
r_matrix[state_4][state_5] = 100
r_matrix[state_5][state_5] = 100
r_matrix[state_3][state_1] = 30

actions_from_0 = [state_4]
actions_from_1 = [state_3, state_5]
actions_from_2 = [state_3]
actions_from_3 = [state_1, state_2, state_4]
actions_from_4 = [state_0, state_3, state_5]
actions_from_5 = [state_1, state_4, state_5]
actions = [actions_from_0,
           actions_from_1,
           actions_from_2,
           actions_from_3,
           actions_from_4,
           actions_from_5]


def get_max_q(q_state):
    q_state_actions = actions[q_state]
    max_q = 0.0

    for action in q_state_actions:
        action_q = q_matrix[q_state][action]
        max_q = max(max_q, action_q)

    return max_q



for i in range(episodes):
    state = random.choice(states)  # randomly select index start state for episode


    while state != goal_state:
        state_actions = actions[state]  # get actions for state
        next_state = random.choice(state_actions)  # randomly select an action (i.e. the next state) of the current state

        q = q_matrix[state][next_state]
        next_q = get_max_q(next_state)
        reward = r_matrix[state][next_state]

        # update Q matrix
        new_q = q + alpha * (reward + gamma * next_q - q)
        q_matrix[state][next_state] = new_q

        # continue with next_state
        state = next_state


# print q_matrix
print(np.matrix(q_matrix))

# print room map
print_map()
print()

# print readable policy
for i in states:
    for j in states:
        if q_matrix[i][j] > 0.0:
            print("From {0} to {1}: {2}".format(i, j, round(q_matrix[i][j], 2)))