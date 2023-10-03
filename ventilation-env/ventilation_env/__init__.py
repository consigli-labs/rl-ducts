from gymnasium.envs.registration import register
from .ventilation import PipesEnv

register(
    id="Ventilation",
    entry_point="ventilation_env:PipesEnv",
    max_episode_steps=600,
)
