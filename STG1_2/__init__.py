from otree.api import *


doc = """
Stage 1 Game
"""


class C(BaseConstants):
    NAME_IN_URL = 'STG1_2'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 2

    # Payoff Dictionaries
    p1_payoff = {
        1: {1: 200, 2: 0},
        2: {1: 300, 2: 100}
    }
    p2_payoff = {
        1: {1: 200, 2: 300},
        2: {1: 0, 2: 100}
    }

    # Roles
    player1_ROLE = 'Player 1'
    player2_ROLE = 'Player 2'

class Subsession(BaseSubsession):
    # Grouping randomly
    def creating_session(self):
        self.group_randomly()

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Setting choice field
    decision = models.StringField()

    # Instructions Quiz
    completedquiz = models.BooleanField(initial=False)

    # History
    @property
    def other(self):
        return self.get_others_in_group()[0]

    def total_payoff(self):
        total_payoff = sum([p.payoff for p in self.in_all_rounds()])
        return total_payoff
    def Stage(self):
        return 1

# PAGES
class Instructions(Page):
    def is_displayed(player: Player):
        return player.round_number == 1

class InstructionsQuiz(Page):
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def live_method(player: Player, data):
        correct_answers = [True, True, 0, 300]
        player_answers = data['Q1', 'Q2', 'Q3', 'Q4']
        if correct_answers == player_answers:
            return player.completedquiz == True

class Decision_Players(Page):
    form_model = 'player'
    form_fields = ['decision']

class ResultsWaitPage(WaitPage):
    # Calculating round payoffs
    def after_all_players_arrive(group: Group):
        player1 = group.get_player_by_role(C.Player1_ROLE)
        player2 = group.get_player_by_role(C.Player2_ROLE)
        if player1.decision == 'A':
            if player2.decision == 'C':
                player1.payoff = C.payoff_AC
                player2.payoff = C.payoff_AC
            else:
                player1.payoff = C.payoff_low
                player2.payoff = C.payoff_high
        else:
            if player2.decision == 'C':
                player1.payoff = C.payoff_high
                player2.payoff = C.payoff_low
            else:
                player1.payoff = C.payoff_BD
                player2.payoff = C.payoff_BD

class PlayerResults(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(history=player.in_all_rounds())

class Stage1End(Page):
    def is_displayed(player: Player):
        return Player.round_number == C.NUM_ROUNDS


page_sequence = [Instructions, InstructionsQuiz, Decision_Players, ResultsWaitPage, PlayerResults, Stage1End]
