import random
from .FourInARowEnv import FourInARowEnv
from .FourInARowAgent import FourInARowAgent

class FourInARowSemiRandomAgent(FourInARowAgent):
  def __init__(self, env: FourInARowEnv) -> None:
    super().__init__(env)

  def get_move(self) -> int:
    possible_actions = self.env.get_possible_actions()

    if len(possible_actions) == 0:
      raise Exception('no possible moves available')

    action = next((action for action in possible_actions if self.env.get_reward_for_action(action) == 1), None)

    return action if action else random.choice(possible_actions)
