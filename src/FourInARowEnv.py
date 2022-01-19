from typing import Optional

from .FourInARowAgent import FourInARowAgent
from .BoxState import BoxState
from .Players import Players
from .FourInARowState import FourInARowState
from .FourInARowRenderer import FourInARowRenderer
from copy import deepcopy

def player_from_box_state(box_state: BoxState) -> Optional[Players]:
  match box_state:
    case BoxState.EMPTY : return None
    case BoxState.RED   : return Players.RED
    case BoxState.YELLOW: return Players.YELLOW

class FourInARowEnv():
  _state   : FourInARowState
  _renderer: FourInARowRenderer
  _yellow_agent: FourInARowAgent
  _possible_states: Optional[list[FourInARowState]]

  def __init__(self, yellow_agent, width: int = 7, height: int = 6, first_turn: Players = Players.RED, win_condition: int = 4) -> None:
    self._state    = FourInARowState(width=width, height=height, first_turn=first_turn, win_condition=win_condition)
    self._renderer = FourInARowRenderer(self._state)
    self._yellow_agent = yellow_agent(self, Players.YELLOW)
    self._possible_states = None

  def reset(self) -> None:
    self._state.reset()

  def step(self, action: int) -> None:
    made_turn = False
    if self._state.get_player_turn() == Players.RED:
      self._state.place_chip(action)
      made_turn = True
      
    if not self.is_done():
      move = self._yellow_agent.get_move()
      self._state.place_chip(move)

    if not made_turn and not self.is_done():
      self._state.place_chip(action)

  def render(self) -> str:
    return self._renderer.render()

  def get_state(self) -> FourInARowState:
    return self._state

  def get_possible_actions(self, state: Optional[FourInARowState] = None) -> list[int]:
    if state is None:
      state = self._state

    if state.is_finished():
      return []
    
    return [column for column in range(state.width) if not state.is_column_full(column)]

  def is_done(self) -> bool:
    return self._state.is_finished()

  def get_reward_for_state(self, state: FourInARowState, player: Players) -> int:
    winner = state.get_winner()
    if winner != None:
      if winner == player:
        return 1
      else:
        return -1
    else:
      return 0

  def _calculate_possible_states(self, state: FourInARowState) -> list[FourInARowState]:
    possible_states = []

    actions = self.get_possible_actions(state)
    for action in actions:
      new_state = deepcopy(state)

      new_state.place_chip(action)

      possible_states.append(new_state)
      if not new_state.is_finished():
        possible_states.extend(self._calculate_possible_states(new_state))

    return possible_states

  def get_possible_states(self) -> list[FourInARowState]:
    if self._possible_states == None:
      self._possible_states = self._calculate_possible_states(self._state)

    return self._possible_states

  def get_state_for_action(self, action: int, state: Optional[FourInARowState] = None) -> FourInARowState:
    if state == None:
      state = self._state
    state_after = deepcopy(state)
    state_after.place_chip(action)
    return state_after

  def get_possible_states_after_action(self, state: FourInARowState, action: int) -> list[FourInARowState]:
    state_after = deepcopy(state)
    state_after.place_chip(action)

    if state_after.is_finished():
      return [state_after]

    result = []
    for a in self.get_possible_actions(state_after):
      copy = deepcopy(state_after)
      copy.place_chip(a)
      result.append(copy)
    return result

  def get_transition_prob(self, action: int, new_state: FourInARowState, old_state: Optional[FourInARowState] = None) -> float:
    if old_state is None:
      old_state = self._state

    if old_state.is_finished():
      return 0.0

    if old_state.is_column_full(action):
      return 0.0
    
    state_after = deepcopy(old_state)
    state_after.place_chip(action) 

    if state_after.is_finished():
      if state_after.get_grid() == new_state.get_grid():
        return 1.0
      else:
        return 0.0
    
    possible_new_states = [] 
    possible_opponent_actions = self.get_possible_actions(state_after)
    for a in possible_opponent_actions:
      possible_new_state = deepcopy(state_after)
      possible_new_state.place_chip(a) 
      possible_new_states.append(possible_new_state.get_grid())
    if new_state.get_grid() not in possible_new_states:
      return 0.0

    prob = 1 / len(possible_new_states)
    return prob
