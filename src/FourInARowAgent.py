from .Players import Players
from .FourInARowEnv import FourInARowEnv

class FourInARowAgent:
  env: FourInARowEnv
  player: Players

  def __init__(self, player: Players, env: FourInARowEnv) -> None:
    self.env = env
    self.player = player

  def do_move(self) -> None:
    pass
