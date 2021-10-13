from pettingzoo.classic import texas_holdem_v4, go_v5

env = texas_holdem_v4.env(num_players=2)
env = go_v5.env(board_size = 19, komi = 7.5)
from pettingzoo.utils import random_demo
random_demo(env, render=True, episodes=10)