from pettingzoo.atari import space_invaders_v1, double_dunk_v2

env = space_invaders_v1.env()
env = double_dunk_v2.env()

from pettingzoo.utils import random_demo
random_demo(env, render=True, episodes=10)

