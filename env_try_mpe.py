from pettingzoo.mpe import simple_adversary_v2, simple_world_comm_v2, simple_speaker_listener_v3

env = simple_adversary_v2.env(N=2, max_cycles=25, continuous_actions=False)

env = simple_world_comm_v2.env(num_good=2, num_adversaries=4, num_obstacles=1,
                num_food=2, max_cycles=25, num_forests=2, continuous_actions=False)

env = simple_speaker_listener_v3.env(max_cycles=25, continuous_actions=False)

from pettingzoo.utils import random_demo
random_demo(env, render=True, episodes=10)