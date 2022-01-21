from copy import deepcopy

from ..FourInARowAgent import FourInARowAgent
from ..Players import Players
from ..FourInARowState import FourInARowState
from ..FourInARowEnv import FourInARowEnv


class FourInARowValueIterationAgent(FourInARowAgent):
  def get_initial_utility(self) -> dict[tuple, float]:
    result = {}
    for s in self.env.get_possible_states():
      result[s.get_grid_as_tuple()] = self.env.get_reward_for_state(s, self.player)
    return result


  def get_q_value(self, state: FourInARowState, action: int, utility: dict[tuple, float]) -> float:
    result = 0.0
    for sp in self.env.get_possible_states_after_action(state, action):
      p = self.env.get_transition_prob(action, sp, state)
      r = self.env.get_reward_for_state(state, self.player)
      result += p * (r + utility[sp.get_grid_as_tuple()])
    return result

  def value_iteration(self, error: float) -> dict[tuple, float]:
    utility = self.get_initial_utility()
    delta = float('inf')
    while delta > error:
      old_utility = utility.copy()

      delta = 0
      for s in self.env.get_possible_states():
        grid_tuple = s.get_grid_as_tuple()
        actions = self.env.get_possible_actions(s)
        if not actions:
          continue
        max_a = max([self.get_q_value(s, a, utility) for a in actions])
        utility[grid_tuple] = max_a
        diff = abs(utility[grid_tuple] - old_utility[grid_tuple])
        if diff > delta:
          delta = diff
    return utility

  _utility: dict[tuple, float]

  def __init__(self, env: FourInARowEnv, player: Players = Players.RED, error: float = 0.00001) -> None:
    super().__init__(env, player)
    self._utility = self.value_iteration(error)
  
  def get_move(self) -> int:
    result = 0
    max_utility = float('-inf')
    for a in self.env.get_possible_actions():
      copy = deepcopy(self.env.get_state())
      copy.place_chip(a)
      value = self._utility[copy.get_grid_as_tuple()]
      if value > max_utility:
        max_utility = value
        result = a

    return result

  def get_transition_probability(self, possible_states: list[FourInARowState], new_state: FourInARowState) -> float:
    return 1 / len(possible_states) # TODO: Implement this
