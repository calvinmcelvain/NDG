from otree.api import *

doc = """
Experiment Wait-room: Sets group matrix and assigns player roles
"""


class C(BaseConstants):
    NAME_IN_URL = 'start'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# Functions
def creating_session(subsession):
    # Creating and storing player roles
    for player in subsession.get_players():
        if player.id_in_group == 1:
            player.participant.vars['role'] = 'Player 1'
        else:
            player.participant.vars['role'] = 'Player 2'


# PAGES
class ExperimentWaitRoom(WaitPage):
    title_text = 'Experiment will start soon'
    body_text = 'Please wait patiently'
    wait_for_all_groups = True


page_sequence = [ExperimentWaitRoom]
