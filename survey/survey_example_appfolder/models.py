from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
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

        for p in self.get_players():
            p.ba_group_assignment = random.Random().randint(0, 3)
            p.ba_ideology_assignment = random.Random().randint(0,1)


class Group(BaseGroup):
    counter = models.IntegerField(initial=0)


class Player(BasePlayer):

    # Variables in order
    ba_group_assignment = models.IntegerField()
    ba_ideology_assignment = models.IntegerField()
    ba_ballot1 = models.IntegerField(initial=-999)
    ba_ballot_pic1 = models.IntegerField(initial=-999)
    party_preference = models.IntegerField(initial=-999)
    household_income = models.IntegerField(initial=-999)
    In_welchem_Land_sind_Sie_geboren = models.StringField(blank=True)
    In_welchem_Land_ist_Ihre_Mutter_geboren = models.StringField(blank=True)
    In_welchem_Land_ist_Ihr_Vater_geboren = models.StringField(blank=True)
    eligibility = models.IntegerField(initial=-999)
    participation = models.IntegerField(initial=-999)
    social_media = models.IntegerField(initial=-999)
    ba_positioning = models.IntegerField(initial=-999)
    ba_party_pos = models.IntegerField(initial=-999)
    ba_opinion1 = models.IntegerField(initial=-999)
    ba_opinion2 = models.IntegerField(initial=-999)
    ba_opinion3 = models.IntegerField(initial=-999)
    ba_opinion4 = models.IntegerField(initial=-999)
    ba_opinion5 = models.IntegerField(initial=-999)
    ba_women1 = models.IntegerField(initial=-999)
    ba_women2 = models.IntegerField(initial=-999)
    ba_women3 = models.IntegerField(initial=-999)
    ba_women4 = models.IntegerField(initial=-999)
    ba_women5 = models.IntegerField(initial=-999)
    ba_women6 = models.IntegerField(initial=-999)
    ba_women7 = models.IntegerField(initial=-999)
    ba_women8 = models.IntegerField(initial=-999)
    ba_women9 = models.IntegerField(initial=-999)
    ba_women10 = models.IntegerField(initial=-999)
    ba_men1 = models.IntegerField(initial=-999)
    ba_men2 = models.IntegerField(initial=-999)
    ba_men3 = models.IntegerField(initial=-999)
    ba_men4 = models.IntegerField(initial=-999)
    ba_men5 = models.IntegerField(initial=-999)
    ba_men6 = models.IntegerField(initial=-999)
    ba_men7 = models.IntegerField(initial=-999)
    ba_men8 = models.IntegerField(initial=-999)
    ba_men9 = models.IntegerField(initial=-999)
    ba_men10 = models.IntegerField(initial=-999)

    # custom error message
    # has to:
    # 1) be in the class Player (important to indent the right way)
    # 2) have a specific name "variablename"_error_message
    def please_state_your_age_error_message(player, value):
        if value < 18:
            return 'You are too young to participate in this survey!'

