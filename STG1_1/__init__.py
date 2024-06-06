from otree.api import *
from settings import INSTRUCTIONS_TIME


doc = """
Stage 1 Instructions
"""


class C(BaseConstants):
    NAME_IN_URL = 'STG1_1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Timeout seconds
    instructions_time = None
    quiz_time = None

    # Payoff Dictionaries
    p1_payoff = {
        1: {1: 200, 2: 0},
        2: {1: 300, 2: 100}
    }
    p2_payoff = {
        1: {1: 200, 2: 300},
        2: {1: 0, 2: 100}
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Page continue validation field
    all_players_ready = models.IntegerField(initial=0)


class Player(BasePlayer):
    pass


# PAGES
class P1(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P2(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P3(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P4(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


class P5(Page):
    timeout_seconds = C.instructions_time

    @staticmethod
    def vars_for_template(player):
        p2_payoff_table = {key: list(value.values()) for key, value in C.p2_payoff.items()}
        p1_payoff_table = {key: list(value.values()) for key, value in C.p1_payoff.items()}
        return {'p1_table': p1_payoff_table, 'p2_table': p2_payoff_table}

    @staticmethod
    def live_method(player: Player, data):
        player.group.all_players_ready += 1
        players_in_session = len(player.subsession.get_players())
        if player.group.all_players_ready == players_in_session:
            player.group.all_players_ready = 0
            return {0: 'all_ready'}


page_sequence = [P1, P2, P3, P4, P5]
