from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Stage_1'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 10
    #Payoffs
    payoff_AC = 200
    payoff_BD = 100
    payoff_low = 0
    payoff_high = 300
    #Roles
    Player1_ROLE = 'Player 1'
    Player2_ROLE = 'Player 2'

class Subsession(BaseSubsession):
    #Grouping randomly
    def creating_session(self):
        self.group_randomly()

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    #Setting choice field
    decision = models.StringField(
        choices=[['C', 'A'], ['D', 'B'], ['C', 'C'], ['D', 'D']],
        widget=widgets.RadioSelect,
    )
    #Geting other players history
    @property
    def other(self):
        return self.get_others_in_group()[0]

    #Practice Quiz Questions
    qrole = models.BooleanField(label="1) If I am assigned the role of player 1 at the beginning of Stage 1, I will be a Player 1 for all rounds of Stage 1.")
    qrandom = models.BooleanField(label="2) If I am assigned the role of Player 2 at the beginning of Stage 1, in each round I will be randomly matched with a different person in the role of Player 1.")
    qplayer1payoff = models.IntegerField(label="3) You are assigned the role of Player 1 at the beginning of Stage 1. If you choose A and the Player 2 matched with you chooses D, your payoff in ECUs is ___", min=0, max=300)
    qotherplayerpayoff = models.IntegerField(label="4) You are assigned the role of Player 2 at the beginning of Stage 1. If you choose C and the Player 1 matched with you chooses B, the other person's payoff in ECUs is ___", min=0, max=300)

# PAGES
class Instructions(Page):
    def is_displayed(player: Player):
        return player.round_number == 1

class InstructionsQuiz(Page):
    form_model = 'player'
    form_fields = ['qrole', 'qrandom', 'qplayer1payoff', 'qotherplayerpayoff']
    def is_displayed(player: Player):
        return player.round_number == 1

class QuizResults(Page):
    def is_displayed(player: Player):
        return player.round_number == 1

class Decision_Players(Page):
    form_model = 'player'
    form_fields = 'decision'

class ResultsWaitPage(WaitPage):
    #Defining payoffs
    @staticmethod
    def after_all_players_arrive(group: Group):
        player1 = group.get_player_by_role(C.Player1_ROLE)
        player2 = group.get_players(C.Player2_ROLE)
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
    pass




page_sequence = [Instructions, InstructionsQuiz, QuizResults ,Decision_Players, ResultsWaitPage, PlayerResults]
