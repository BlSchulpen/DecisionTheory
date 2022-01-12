from typing import Generic, Optional, TypeVar
from numpy.lib.function_base import select

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
  _yellow_agent = FourInARowAgent

  def __init__(self, yellow_agent, width: int = 7, height: int = 6, first_turn: Players = Players.RED) -> None:
    self._state    = FourInARowState(width=width, height=height, first_turn=first_turn)
    self._renderer = FourInARowRenderer(self._state)
    self._yellow_agent = yellow_agent(self)

  def _calculate_possible_states(self, state: FourInARowState) -> list[FourInARowState]:
    possible_states = []

    actions = self.get_possible_actions(state)
    for action in actions:
      new_state = deepcopy(state)

      new_state.place_chip(action)

      possible_states.append(new_state)
      if not self.is_done(new_state):
        possible_states.extend(self._calculate_possible_states(new_state))

    return possible_states

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

  def get_reward_for_action(self, action: int) -> int:
    if self.is_done():
      return 0

    new_state = deepcopy(self._state)
    new_state.place_chip(action)
    if new_state.get_winner() != None:
      return 1
    else:
      return -1

  def get_transition_prob(self, action: int, old_state:FourInARowState, new_state:FourInARowState):
    if old_state is None:
       old_state = self._state

    if self.is_done(old_state):
      return 0.0

    if old_state.is_column_full(action):
      return 0.0
    
    state_after = deepcopy(old_state)
    state_after.place_chip(action) 

    if self.is_done(state=state_after) and state_after == new_state:
      return 1.0
    
    possible_new_states = [] 

    possible_opponent_actions = self.get_possible_actions(state=state_after)
    for action in possible_opponent_actions:
      possible_new_state = deepcopy(state_after)
      possible_new_state.place_chip(action) 
      possible_new_states.append(possible_new_state)
    if new_state not in possible_new_states:
      return 0.0

    prob = 1 / len(possible_new_states)
    return prob