from pettingzoo.sisl import multiwalker_v7, pursuit_v3, waterworld_v3
import numpy as np

env = multiwalker_v7.env(n_walkers=3, position_noise=1e-3, angle_noise=1e-3,
local_ratio=1.0, forward_reward=1.0, terminate_reward=-100.0, fall_reward=-10.0,
terminate_on_fall=True, remove_on_fall=True, max_cycles=500)

env = pursuit_v3.env(max_cycles=500, x_size=16, y_size=16, local_ratio=1.0, n_evaders=30,
n_pursuers=8,obs_range=7, n_catch=2, freeze_evaders=False, tag_reward=0.01,
catch_reward=5.0, urgency_reward=0.0, surround=True, constraint_window=1.0)

# env = waterworld_v3.env(n_pursuers=5, n_evaders=5, n_poison=10, n_coop=2, n_sensors=20,
# sensor_range=0.2,radius=0.015, obstacle_radius=0.2,
# obstacle_coord=np.array([0.5, 0.5]), pursuer_max_accel=0.01, evader_speed=0.01,
# poison_speed=0.01, poison_reward=-1.0, food_reward=10.0, encounter_reward=0.01,
# thrust_penalty=-0.5, local_ratio=1.0, speed_features=True, max_cycles=500)

from pettingzoo.utils import random_demo
random_demo(env, render=True, episodes=1)