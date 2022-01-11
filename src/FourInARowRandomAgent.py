import random
from .Players import Players
from .FourInARowEnv import FourInARowEnv
from .FourInARowAgent import FourInARowAgent

class FourInARowRandomAgent(FourInARowAgent):
  def __init__(self, player: Players, env: FourInARowEnv) -> None:
    super().__init__(player, env)

  def do_move(self) -> None:
    possible_moves = self.env.get_possible_actions()

    if len(possible_moves) == 0:
      raise Exception('no possible moves available')

    self.env.place_chip(self.player, random.choice(possible_moves))
