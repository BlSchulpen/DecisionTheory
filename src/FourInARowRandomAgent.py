import random
from .FourInARowEnv import FourInARowEnv
from .FourInARowAgent import FourInARowAgent

class FourInARowRandomAgent(FourInARowAgent):
  def __init__(self, env: FourInARowEnv) -> None:
    super().__init__(env)

  def get_move(self) -> int:
    possible_moves = self.env.get_possible_actions()

    if len(possible_moves) == 0:
      raise Exception('no possible moves available')

    return random.choice(possible_moves)
