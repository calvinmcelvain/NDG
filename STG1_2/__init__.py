from otree.api import *
from settings import DECISION_TIME, FEEDBACK_TIME

doc = """
Stage 1 Game
"""


class C(BaseConstants):
    NAME_IN_URL = 'STG1_2'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 5

    # Payoff Dictionaries
    p1_payoff = {
        'A': {'C': 200, 'D': 0},
        'B': {'C': 300, 'D': 100}
    }
    p2_payoff = {
        'A': {'C': 200, 'D': 300},
        'B': {'C': 0, 'D': 100}
    }

    # Roles
    p1_ROLE = 'Player 1'
    p2_ROLE = 'Player 2'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Form fields
    decision = models.StringField()

    # History
    def other(self):
        return self.get_others_in_group()[0]
    

    def total_payoff(self):
        total_payoff = sum([p.payoff for p in self.in_all_rounds()])
        return total_payoff
    

# Functions
def creating_session(subsession):
    subsession.group_randomly(fixed_id_in_group=True)
    

# PAGES
class Decision_1(Page):
    form_model = 'player'
    form_fields = ['decision']


class PayoffWaitPage(WaitPage):
    # Calculating round payoffs
    def after_all_players_arrive(group: Group):
        player1 = group.get_player_by_role(C.Player1_ROLE)
        player2 = group.get_player_by_role(C.Player2_ROLE)
        player1.payoff = C.p1_payoff[player1.decision][player2.decision]
        player2.payoff = C.p2_payoff[player1.decision][player2.decision]


class Results_2(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(history=player.in_all_rounds())


page_sequence = [Decision_1, PayoffWaitPage, Results_2]
