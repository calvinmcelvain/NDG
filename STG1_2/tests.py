from otree.api import Currency as c, currency_range, expect, Bot
from . import *
import random as r


class PlayerBot(Bot):
    def play_round(self):
        p1 = ['A', 'B']
        p2 = ['C', 'D']
        if self.player.role == 'Player 1':
            yield Submission(P1_Decision, dict(decision=r.choice(p1)), check_html=False)
            yield Submission(P2_Results, check_html=False)
        else:
            yield Submission(P1_Decision, dict(decision=r.choice(p2)), check_html=False)
            yield Submission(P2_Results, check_html=False)