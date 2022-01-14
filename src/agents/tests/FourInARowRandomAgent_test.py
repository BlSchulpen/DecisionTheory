from unittest import TestCase, main
from src import FourInARowEnv, Players, BoxState
from .. import FourInARowRandomAgent, FourInARowRandomAgent

class Test_FourInARowRandomAgent(TestCase):
  def test_move_allowed(self):
    # Arrange 

    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.RED
    )

    agent = FourInARowRandomAgent(env=env)


    env._state._grid = [
      [BoxState.RED   , BoxState.EMPTY ],
      [BoxState.RED, BoxState.RED ]
    ]
    
    expected_move = 0
    
    # Act
    result = agent.get_move()

    # Assert
    self.assertEqual(expected_move,result)

if __name__ == '__main__':
  main()
