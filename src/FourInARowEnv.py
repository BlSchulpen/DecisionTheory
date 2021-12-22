from .Players import Players
from .FourInARowState import FourInARowState
from .FourInARowRenderer import FourInARowRenderer

class FourInARowEnv:
  _state   : FourInARowState
  _renderer: FourInARowRenderer

  def _calculate_possible_states(self):
    pass

  def _calculate_transition(self, action):
    pass

  def __init__(self, width: int = 7, height: int = 6, first_turn: Players = Players.RED) -> None:
    self._state    = FourInARowState(width=width, height=height, first_turn=first_turn)
    self._renderer = FourInARowRenderer(self._state)

  def reset(self) -> None:
    self._state.reset()

  def step(self, action):
    pass

  def render(self) -> str:
    return self._renderer.render()

  def get_possible_states(self):
    pass

  def get_possible_actions(self):
    pass

  def is_done(self) -> bool:
    for i in range(6):
        print('row nr:' + str(i))
        for j in range(7):   
            print(self._state.get_grid()[j][i])
    return False


  # def is_row_done(self) -> bool:
  #   for spot in self._state.get_grid:
  #     print("test")
  #   return False

  def get_reward(self):
    pass

  def get_transition_prob(self, action):
    pass