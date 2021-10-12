from pettingzoo.butterfly import prison_v3, prospector_v4, knights_archers_zombies_v7, pistonball_v4, cooperative_pong_v3

env = prospector_v4.env(ind_reward=0.8, group_reward=0.1, other_group_reward=0.1,
prospec_find_gold_reward=1, prospec_handoff_gold_reward=1, banker_receive_gold_reward=1,
banker_deposit_gold_reward=1, max_cycles=150)

env = knights_archers_zombies_v7.env(spawn_rate=20, num_knights=2, num_archers=2,
killable_knights=True, killable_archers=True, line_death=True, pad_observation=True,
max_cycles=900)

env = pistonball_v4.env()

env = cooperative_pong_v3.env(ball_speed=9, left_paddle_speed=12,
right_paddle_speed=12, cake_paddle=True, max_cycles=900, bounce_randomness=False)

env = prison_v3.env(vector_observation=False, continuous=False, synchronized_start=False,
identical_aliens=False, max_cycles=150, num_floors=4, random_aliens=False)

from pettingzoo.utils import random_demo
random_demo(env, render=True, episodes=1)