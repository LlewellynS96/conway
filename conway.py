import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.signal import convolve2d


def create_board(n):
    board = np.zeros((n, n))
    mask = np.random.choice(2, (n, n), p=[0.5, 0.5]).astype(np.bool)
    board[mask] = 1.
    return board


def perturb_board(board):
    neighbours = convolve2d(board, np.ones((3, 3)), 'same', 'wrap') - board
    board[(neighbours < 2) | (neighbours > 3)] = 0.
    board[neighbours == 3] = 1.


def update(n):
    if n == 0:
        return
    perturb_board(board)
    im.set_data(board)


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--size', type=int, default=100)
parser.add_argument('-f', '--frames', type=int, default=1000000)
parser.add_argument('-w', '--wait', type=int, default=1)
args = parser.parse_args()
board = create_board(args.size)
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'xticks': [], 'yticks': []})
im = ax.imshow(board)
animation = FuncAnimation(fig, func=update, frames=args.frames, interval=args.wait, repeat=False)
plt.show()
