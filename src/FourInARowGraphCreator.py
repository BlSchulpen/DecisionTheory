from lib2to3.pgen2.pgen import generate_grammar
from tkinter import W
from unittest import result
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from .FourInARowEnv import FourInARowEnv
from .FourInARowRandomAgent import FourInARowRandomAgent
from .FourInARowValueIterationAgent import FourInARowValueIterationAgent
from .FourInARowSemiRandomAgent import FourInARowSemiRandomAgent
from .FourInARowMinMaxAgent import FourInARowMinMaxAgent

from .Players import Players
from copy import deepcopy

import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 


#TODO add graph preformance (time)
#TODO add graphs win ratio


class FourInARowGameResults:
    wins: int
    ties: int
    loses: int
    agent: str

    def __init__(self,wins:int,ties:int,loses:int,agent: str) -> None:
        self.wins = wins
        self.loses = loses
        self.ties = ties
        self.agent = agent

class FourInARowGraphCreator:
    value_iterator_agent: FourInARowValueIterationAgent
    random_agent: FourInARowRandomAgent
    semi_random_agen: FourInARowSemiRandomAgent
    min_max_agen: FourInARowMinMaxAgent

    def __init__(self) -> None:
        pass 
        # self.random_agent = FourInARowRandomAgent
        # self.semi_random_agen = FourInARowSemiRandomAgent
        # self.setup_value_iterator_agent()
        # self.setup_min_max_agent()


    def setup_game(self,opponent) -> FourInARowEnv:
        env = FourInARowEnv(
            yellow_agent  = opponent,
            width         = 3,
            height        = 3,
            win_condition = 3,
            first_turn    = Players.RED
        )
        return env

    #TODO add new graphs to also show ties + loses
    def ratio_value(self, main_type,opponent_type) -> None:
        nr_games = 1
        nr_wins = 0 
        for i in range(nr_games): #TODO frist test graph generation
            env = self.setup_game(FourInARowRandomAgent)
            value_iterator = FourInARowMinMaxAgent(env)
            while not env.is_done():
                env.step(value_iterator.get_move())
            if env._state.get_winner() == Players.RED:
                nr_wins +=1
    
    def test(self):
        result_one = FourInARowGameResults(wins=10,loses=5, ties=5,agent="test agent")
        result_two = FourInARowGameResults(wins=10,loses=9, ties=1,agent="test2 agent")
        self.generate_graph([result_one,result_two])

    def generate_graph(self, results:list[FourInARowGameResults]) -> None:        
        # create data
        x = []
        for item in results:
            x.append(item.agent)

        y1 = np.array([results[0].wins, results[1].wins])
        y2 = np.array([results[0].ties, results[1].ties])
        y3 = np.array([results[0].loses, results[1].loses])

        # plot bars in stack manner
        plt.bar(x, y1, color='g')
        plt.bar(x, y2, bottom=y1, color='y')
        plt.bar(x, y3, bottom=y1+y2, color='r')

        plt.xlabel("Teams")
        plt.ylabel("Score")
        plt.legend(["Wins", "Ties", "Loses"])
        plt.title("Scores by Teams in 4 Rounds")
        plt.show()
    def win_ration(self,nr_games, nr_wins) -> float:
        return (100*nr_wins)/nr_games