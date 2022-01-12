from typing import Generic, Optional, TypeVar
from numpy.lib.function_base import select

from .FourInARowAgent import FourInARowAgent
from .BoxState import BoxState
from .Players import Players
from .FourInARowState import FourInARowState
from .FourInARowRenderer import FourInARowRenderer
from copy import copy

def player_from_box_state(box_state: BoxState) -> Optional[Players]:
  match box_state:
    case BoxState.EMPTY : return None
    case BoxState.RED   : return Players.RED
    case BoxState.YELLOW: return Players.YELLOW

class FourInARowEnv():
  _state   : FourInARowState
  _renderer: FourInARowRenderer
  _yellow_agent = FourInARowAgent

  def __init__(self, yellow_agent, width: int = 7, height: int = 6, first_turn: Players = Players.RED) -> None:
    self._state    = FourInARowState(width=width, height=height, first_turn=first_turn)
    self._renderer = FourInARowRenderer(self._state)
    self._yellow_agent = yellow_agent(self)

  def _calculate_possible_states(self, state: FourInARowState) -> list[FourInARowState]:
    possible_states = []

    actions = self.get_possible_actions(state)
    for action in actions:
      new_state = copy(state)

      new_state.place_chip(action)

      possible_states.append(new_state)
      if not self.is_done(new_state):
        possible_states.extend(self._calculate_possible_states(new_state))

    return possible_states

  def _calculate_transition(self, action):
    pass

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

  def get_possible_states(self):
    return self._calculate_possible_states(self._state)

  def get_possible_actions(self, state: FourInARowState = None) -> list[int]:
    if state is None:
      state = self._state
    return [column for column in range(state.width) if not state.is_column_full(column)]

  def is_done(self) -> bool:
    winner = self._state.get_winner()
    full = self._state.is_full()
    return winner != None or full

  def get_reward(self):
    pass

  def get_transition_prob(self, action):
    pass

  # Possible actions methods

  def _get_highest_possible(self,x):
    for j in range(self._state.height):
      if self._state.get_grid()[x][j] == BoxState.EMPTY:
        return (x,j)
    return False
