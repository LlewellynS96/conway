import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

BOARD = None


def create_board(n):
    global BOARD
    BOARD = np.zeros((n, n))
    mask = np.random.choice(2, BOARD.shape, p=[0.5, 0.5]).astype(np.bool)
    BOARD[mask] = 1


def count_neighbours(board):
    neighbours = np.zeros(board.shape)
    neighbours[:-1, :-1] += board[1:, 1:]
    neighbours[1:, :-1] += board[:-1, 1:]
    neighbours[:-1, 1:] += board[1:, :-1]
    neighbours[1:, 1:] += board[:-1, :-1]
    neighbours[:-1, :] += board[1:, :]
    neighbours[1:, :] += board[:-1, :]
    neighbours[:, :-1] += board[:, 1:]
    neighbours[:, 1:] += board[:, :-1]

    return neighbours


def perturb_board(board):
    neighbours = count_neighbours(board)
    rule_one = neighbours < 2
    board[rule_one] = 0.
    rule_three = neighbours == 3
    board[rule_three] = 1.
    rule_four = neighbours > 3
    board[rule_four] = 0.
    return board


def show_board(board):
    plt.imshow(board)
    plt.draw()


def step(n):
    global BOARD
    if n == 0:
        return
    BOARD = perturb_board(BOARD)
    im.set_data(BOARD)


n = 100
s = 100
create_board(n)

# BOARD = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 1, 1, 1, 1, 1, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# BOARD = np.array(BOARD)

fig, ax = plt.subplots()
im = ax.imshow(BOARD)
animation = FuncAnimation(fig, func=step, frames=10000, interval=s)

plt.show()
