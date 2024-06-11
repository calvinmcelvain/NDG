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
    
    # Highlighting Grid Dictionary
    grid =  {
        'A': {'C': 1, 'D': 2},
        'B': {'C': 3, 'D': 4}
    }

    # Roles
    p1_ROLE = 'Player 1'
    p2_ROLE = 'Player 2'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    grid = models.FloatField()


class Player(BasePlayer):
    # Form fields
    decision = models.StringField()

    # History
    def other_decision(self):
        return self.get_others_in_group()[0].decision
    
    def other_payoff(self):
        return self.get_others_in_group()[0].payoff

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
    
    @staticmethod
    def vars_for_template(player):
        p2_payoff_table = {key: list(value.values()) for key, value in C.p2_payoff.items()}
        p1_payoff_table = {key: list(value.values()) for key, value in C.p1_payoff.items()}
        return {'p1_table': p1_payoff_table, 'p2_table': p2_payoff_table, 'history': reversed(player.in_previous_rounds())}
    
    @staticmethod
    def js_vars(player):
        return dict(
            timeout=DECISION_TIME,
        )


class PayoffWaitPage(WaitPage):
    # Calculating round payoffs
    def after_all_players_arrive(group: Group):
        player1 = group.get_player_by_role(C.p1_ROLE)
        player2 = group.get_player_by_role(C.p2_ROLE)
        player1.payoff = C.p1_payoff[player1.decision][player2.decision]
        player2.payoff = C.p2_payoff[player1.decision][player2.decision]
        group.grid = C.grid[player1.decision][player2.decision]


class Results_2(Page):
    timeout_seconds = FEEDBACK_TIME
    
    @staticmethod
    def vars_for_template(player: Player):
        p2_payoff_table = {key: list(value.values()) for key, value in C.p2_payoff.items()}
        p1_payoff_table = {key: list(value.values()) for key, value in C.p1_payoff.items()}
        return {'p1_table': p1_payoff_table, 'p2_table': p2_payoff_table, 'history': reversed(player.in_all_rounds())}
    

class BeforeNextRound(WaitPage):
    wait_for_all_groups = True
    title_text = 'Next round will start soon'
    body_text = 'Waiting for other participants'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number != C.NUM_ROUNDS


class BeforeNextStage(WaitPage):
    wait_for_all_groups = True
    title_text = 'End of Stage 1'
    body_text = 'Instructions for Stage 2 will begin when all players are ready'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [Decision_1, PayoffWaitPage, Results_2, BeforeNextRound, BeforeNextStage]
