import random

from ..Players import Players
from ..FourInARowEnv import FourInARowEnv
from ..FourInARowAgent import FourInARowAgent

class FourInARowSemiRandomAgent(FourInARowAgent):
  def _get_utility_for_action(self, action: int) -> int:
    state_after = self.env.get_state_for_action(action)
    if state_after.is_finished():
      return self.env.get_reward_for_state(state_after, self.player)

    for sp in self.env.get_possible_states_after_action(self.env.get_state(), action):
      if self.env.get_reward_for_state(sp, self.player) == -1:
        return -1

    return 0

  def __init__(self, env: FourInARowEnv, player: Players = Players.RED) -> None:
    super().__init__(env, player)

  def get_move(self) -> int:
    possible_actions = self.env.get_possible_actions()
    random.shuffle(possible_actions)

    if len(possible_actions) == 0:
      raise Exception('no possible moves available')

    max_utility = float('-inf')
    best_move = 0
    for a in possible_actions:
      utility = self._get_utility_for_action(a)
      if utility > max_utility:
        max_utility = utility
        best_move = a

    return best_move
