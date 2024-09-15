from random import randint




rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps = {"rock": rock, "paper":paper, "scissors":scissors} # todo: make a dict from the 3 items

def index_to_hand(index):
    for index, value in rps.items():
        return

import os


enumerate(rps)
class Hand:
    def __init__(self,hand_index):
        self.hand_index = int(hand_index)

    def __str__(self):
        return





game_logic = "" # should be int compare to int,

user_move = int(input('choose your move:\n')) # int

script_move = rps[randint(0,2)] # should be int


def eval_results(user_move,script_move):
    pass


