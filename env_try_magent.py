from pettingzoo.magent import adversarial_pursuit_v3, gather_v3, combined_arms_v5, tiger_deer_v3

env = adversarial_pursuit_v3.env(map_size=45, minimap_mode=False, tag_penalty=-0.2,
max_cycles=500, extra_features=False)

env = gather_v3.env(minimap_mode=False, step_reward=-0.01, attack_penalty=-0.1,
dead_penalty=-1, attack_food_reward=0.5, max_cycles=500, extra_features=False)

env = combined_arms_v5.env(map_size=45, minimap_mode=False, step_reward=-0.005,
dead_penalty=-0.1, attack_penalty=-0.1, attack_opponent_reward=0.2, max_cycles=1000,
extra_features=False)

env = tiger_deer_v3.env(map_size=45, minimap_mode=False, tiger_step_recover=-0.1, deer_attacked=-0.1, max_cycles=500, extra_features=False)

from pettingzoo.utils import random_demo
random_demo(env, render=True, episodes=1)