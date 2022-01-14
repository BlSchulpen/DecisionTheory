
from unittest import TestCase, main
from src import FourInARowEnv, FourInARowRandomAgent, Players, render_multiple_states, BoxState, FourInARowRenderer, FourInARowValueIterationAgent
from copy import deepcopy

class Test_FourInARowEnv(TestCase):

  def test_get_reward_win(self):
    # Arrange 

    # should be in setup
    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.RED
    )

    expected_reward = 1
    state = deepcopy(env._state)
    state._grid = [
      [BoxState.RED   , BoxState.RED ],
      [BoxState.RED, BoxState.RED ]
    ]

    # Act 
    actual_reward = env.get_reward_for_state(state, Players.RED)
  
    # Assert
    self.assertEqual(actual_reward, expected_reward)



  def test_get_reward_lose(self):
    # Arrange 
    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.RED
    )
    
    expected_reward = -1
    state = deepcopy(env._state)
    state._grid = [
      [BoxState.YELLOW   , BoxState.YELLOW ],
      [BoxState.YELLOW, BoxState.YELLOW ]
    ]

    # Act 
    actual_reward = env.get_reward_for_state(state, Players.RED)
  
    # Assert
    self.assertEqual(actual_reward, expected_reward)


  def test_get_reward_neutral(self):
    # Arrange 
    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.RED
    )
    
    expected_reward = 0
    state = deepcopy(env._state)
    state._grid = [
      [BoxState.RED   , BoxState.EMPTY ],
      [BoxState.YELLOW, BoxState.EMPTY ]
    ]

    # Act 
    actual_reward = env.get_reward_for_state(state, Players.RED)
  
    # Assert
    self.assertEqual(actual_reward, expected_reward)


   # is done method...
  def test_is_done(self):
    # Arrange 
    env = FourInARowEnv(
        yellow_agent  = FourInARowRandomAgent,
        width         = 2,
        height        = 2,
        win_condition = 2,
        first_turn    = Players.RED
    )
    state = deepcopy(env._state)
    state._grid = [
    [BoxState.RED   , BoxState.YELLOW ],
    [BoxState.YELLOW, BoxState.RED ]
    ]

    env._state = state

    # Act 
    done = env.is_done()

    # Assert
    self.assertTrue(done)