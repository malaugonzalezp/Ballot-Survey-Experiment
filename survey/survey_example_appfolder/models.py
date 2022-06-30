from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Maria, Adam, Fabian, Adam, Miriam, Carlo'
doc = 'Your app description goes here'


class Constants(BaseConstants):
    name_in_url = 'survey-test'
    players_per_group = None
    num_rounds = 1

import random

class Subsession(BaseSubsession):
    def creating_session(self):
        '''this is a function by otree (same can not be changed)
        which is creating a new subsession. Any variables that are needed to be custom
        (so declaring it in a different way before) are created here'''
        for p in self.get_players():
            # here we want to declare the players to different groups (2 in total)
            # we use a python function here from 'random' we imported earlier
            p.group_assignment = random.Random().randint(0, 1)


class Group(BaseGroup):
    counter = models.IntegerField(initial=0)


class Player(BasePlayer):

    # Variables in order
    ba_ballot1 = models.IntegerField(initial=-999)
    ba_ballot = models.IntegerField(initial=-999)
    please_state_your_age = models.IntegerField(max=110, min=1)
    ba_education = models.IntegerField(initial=-999)
    please_state_your_postal_code = models.IntegerField(max=99999, min=10000)
    ba_gender = models.IntegerField(initial=-999)
    ba_hidden_input = models.IntegerField(initial=50, blank=True)
    ba_positioning = models.IntegerField(initial=-999)
    ba_party_pos = models.IntegerField(initial=-999)

    # custom error message
    # has to:
    # 1) be in the class Player (important to indent the right way)
    # 2) have a specific name "variablename"_error_message
    def please_state_your_age_error_message(player, value):
        if value < 18:
            return 'You are too young to participate in this survey!'

