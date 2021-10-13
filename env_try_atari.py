from pettingzoo.atari import space_invaders_v1

env = env = space_invaders_v1.env()

from pettingzoo.utils import random_demo
random_demo(env, render=True, episodes=10)

