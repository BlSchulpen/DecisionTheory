from typing import Optional

from ..FourInARowAgent import FourInARowAgent
from ..Players import Players
from ..FourInARowState import FourInARowState
from ..FourInARowEnv import FourInARowEnv


class FourInARowBruteForceAgent(FourInARowAgent):
  def get_utility(self, state: FourInARowState, action: int) -> float:
    state_after = self.env.get_state_for_action(action, state)
    if state_after.is_finished():
      return self.env.get_reward_for_state(state_after, self.player)

    max_value = float('-inf')
    for new_state in self.env.get_possible_states_after_action(state, action):
      probability = self.env.get_transition_prob(action, new_state, state)
      reward = self.env.get_reward_for_state(new_state, self.player)
      value = probability * (reward + self.get_q_value(new_state))

      if value > max_value:
        max_value = value
    return max_value

  def get_q_value(self, state: FourInARowState) -> float:
    total_value = 0
    for action in self.env.get_possible_actions(state):
      total_value += self.get_utility(state, action)
    return total_value

  def get_highest_utility(self) -> Optional[int]:
    best_action: Optional[int] = None
    max_value = float('-inf')
    for action in self.env.get_possible_actions():
      value = self.get_utility(self.env.get_state(), action)
      if value > max_value:
        max_value = value
        best_action = action
    return best_action

  def __init__(self, env: FourInARowEnv, player: Players = Players.RED) -> None:
    super().__init__(env, player)
  
  def get_move(self) -> int:
    result = self.get_highest_utility()
    if result == None:
      raise Exception('unwrap failed')
    return result
