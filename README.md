# Learning PettingZoo Environments

## API

### Example of initializing environment:

```python
from pettingzoo.butterfly import pistonball_v4
env = pistonball_v4.env()
```

### Interacting with env:

```python
env.reset()
for agent in env.agent_iter():
    observation, reward, done, info = env.last()
    action = policy(observation, agent)
    env.step(action)
```

### Parallel API:

```python
parallel_env = pistonball_v4.parallel_env()
observations = parallel_env.reset()
max_cycles = 500
for step in range(max_cycles):
    actions = {agent: policy(observations[agent], agent) for agent in parallel_env.agents}
    observations, rewards, dones, infos = parallel_env.step(actions)
```

### Full API:

Attributes: `agents`, `num_agents`, `possible_agents`, `max_num_agents`, `observation_spaces`, `action_spaces` 

Methods: `render(mode='human')`, `seed(seed=None)`, `close()`, `observation_space(agent)`, `action_space(agent)`

`step(actions)`: receives a dictionary of actions keyed by the agent name. 
Returns the observation dictionary, reward dictionary, done dictionary, and info dictionary, 
where each dictionary is keyed by the agent.

`reset()`: resets the environment and returns a dictionary of observations (keyed by the agent name)

### Manual control:

Often, you want to be able to play before trying to learn it to get a better feel for it. 
Some of our games directly support this:

```python
from pettingzoo.butterfly import prison_v3
prison_v3.manual_control(<environment parameters>)
```

### Random demo:

You can also easily get a quick impression of them by watching a random policy control all the actions:

```python
from pettingzoo.utils import random_demo
random_demo(env, render=True, episodes=1)
```

## [Enviroonment Creation](https://www.pettingzoo.ml/environment_creation)


## Environments

- [Atari](https://www.pettingzoo.ml/atari)
- [Butterfly](https://www.pettingzoo.ml/butterfly)
- [Classic](https://www.pettingzoo.ml/classic)
- [MAgent](https://www.pettingzoo.ml/magent)
- [MPE](https://www.pettingzoo.ml/mpe)
- [SISL](https://www.pettingzoo.ml/sisl)

## Credits

- [`pettingzoo` website](https://www.pettingzoo.ml/#)
- [TDS | `pettingzoo` tutorial 1](https://towardsdatascience.com/multi-agent-deep-reinforcement-learning-in-15-lines-of-code-using-pettingzoo-e0b963c0820b)
- [TDS | `pettingzoo` tutorial 2](https://towardsdatascience.com/using-pettingzoo-with-rllib-for-multi-agent-deep-reinforcement-learning-5ff47c677abd)








