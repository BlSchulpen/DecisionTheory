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
    nr_games: int

    def __init__(self) -> None:
        self.nr_games = 3

    def setup_game(self,opponent) -> FourInARowEnv:
        env = FourInARowEnv(
            yellow_agent  = opponent,
            width         = 3,
            height        = 3,
            win_condition = 3,
            first_turn    = Players.RED
        )
        return env


    def play_game(self, personal_type,opponent_type) -> FourInARowGameResults:
        nr_wins = 0 
        nr_loses = 0
        nr_ties = 0 
        for i in range(self.nr_games): 
            env = self.setup_game(opponent_type)
            main_agent = personal_type(env)
            while not env.is_done():
                env.step(main_agent.get_move())
            if env._state.get_winner() == Players.RED:
                nr_wins +=1
            elif env._state.get_winner() == Players.YELLOW:
                nr_loses +=1       
            else:
                nr_ties +=1
        val_it_games = FourInARowGameResults(wins=nr_wins,ties=nr_ties,loses=nr_loses,agent=type(main_agent).__name__)
        return val_it_games

    def create_graph_game(self) -> None:
        agent_types = [FourInARowRandomAgent,FourInARowMinMaxAgent, FourInARowMinMaxAgent]
        results = [] 
        for start_agent in agent_types:
            for end_agent in agent_types:
                result = self.play_game(start_agent,end_agent)
                results.append(result)
        self.generate_graph(results)






    def generate_graph(self, results:list[FourInARowGameResults]) -> None:        
        # create data
        x = []
        for item in results:
            x.append(item.agent)

        wins = [] 
        ties = []
        loses = [] 
        for result in results:
            wins.append(result.wins)
            ties.append(result.ties)
            loses.append(result.loses)


        y1 = np.array(wins)
        y2 = np.array(ties)
        y3 = np.array(loses)

        # plot bars in stack manner
        plt.bar(x, y1, color='g')
        plt.bar(x, y2, bottom=y1, color='y')
        plt.bar(x, y3, bottom=y1+y2, color='r')

        plt.xlabel("Teams")
        plt.ylabel("Score")
        plt.legend(["Wins", "Ties", "Loses"])
        plt.title("Result games")
        plt.show()


    def win_ration(self,nr_games, nr_wins) -> float:
        return (100*nr_wins)/nr_games