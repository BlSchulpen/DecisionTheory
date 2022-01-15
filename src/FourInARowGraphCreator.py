from lib2to3.pgen2.pgen import generate_grammar
from tkinter import W
from unittest import result
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from .FourInARowEnv import FourInARowEnv
from src.agents import FourInARowRandomAgent
from src.agents import FourInARowValueIterationAgent
from src.agents import FourInARowSemiRandomAgent
from src.agents import FourInARowMinMaxAgent


from .Players import Players
from copy import deepcopy

import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 


#TODO add graph preformance (time)
#TODO add graphs win ratio
from enum import Enum
class WinType(Enum):
    WIN = 1
    TIE = 2
    LOSE = 3

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
        self.nr_games = 1

    def setup_game(self,opponent) -> FourInARowEnv:
        env = FourInARowEnv(
            yellow_agent  = opponent,
            width         = 3,
            height        = 3,
            win_condition = 3,
            first_turn    = Players.RED
        )
        return env


    def play_game(self, player_type,opponent_type) -> WinType:
        env = FourInARowEnv(
            yellow_agent  = opponent_type,
            width         = 3,
            height        = 3,
            win_condition = 3,
            first_turn    = Players.RED
            )

        agent = player_type(env)
        states = []
        states.append(deepcopy(env.get_state()))
        while not env.is_done():
            env.step(agent.get_move())
            states.append(deepcopy(env.get_state()))
        if env._state.get_winner() == Players.RED:
            return WinType.WIN
        elif env._state.get_winner() == Players.YELLOW:
            return WinType.LOSE
        return WinType.TIE


    def min_max_game(self,opponent_type,name):
        results =  []
        game_results = FourInARowGameResults(0,0,0,"Min Max")
        for i in range(self.nr_games):
            end_state = self.play_game(FourInARowMinMaxAgent,opponent_type)
            if end_state == WinType.WIN:
                game_results.wins +=1
            elif end_state== WinType.LOSE:
                game_results.loses +=1
            else:
                game_results.ties +=1
        results.append(game_results)

        game_results2 = FourInARowGameResults(0,0,0,"Iterative")
        for i in range(self.nr_games):
            end_state = self.play_game(FourInARowValueIterationAgent,opponent_type=opponent_type)
            if end_state == WinType.WIN:
                game_results2.wins +=1
            elif end_state== WinType.LOSE:
                game_results2.loses +=1
            else:
                game_results2.ties +=1
        results.append(game_results2)
        self.generate_graph(results=results,name=name)


    def random_graph(self,opponent_type,name):
        results =  []
        game_results = FourInARowGameResults(0,0,0,"Random agent")
        for i in range(self.nr_games):
            end_state = self.play_game(FourInARowRandomAgent,opponent_type)
            if end_state == WinType.WIN:
                game_results.wins +=1
            elif end_state== WinType.LOSE:
                game_results.loses +=1
            else:
                game_results.ties +=1
        results.append(game_results)

        game_results2 = FourInARowGameResults(0,0,0,"Semi-random agent")
        for i in range(self.nr_games):
            end_state = self.play_game(FourInARowSemiRandomAgent,opponent_type=opponent_type)
            if end_state == WinType.WIN:
                game_results2.wins +=1
            elif end_state== WinType.LOSE:
                game_results2.loses +=1
            else:
                game_results2.ties +=1
        results.append(game_results2)
        self.generate_graph(results=results,name=name)



    def generate_graph(self, results:list[FourInARowGameResults], name: str) -> None:        
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

        plt.xlabel("Agents")
        plt.ylabel("Score")
        plt.legend(["Wins", "Ties", "Loses"])
        plt.title(name)
        plt.show()


    def win_ration(self,nr_games, nr_wins) -> float:
        return (100*nr_wins)/nr_games