from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player

class Welcome(Page):
    form_model = Player

    def before_next_page(self):
        self.group.counter += 1

class DemoPage(Page):
    form_model = Player
    form_fields = ['party_preference1', 'party_preference2', 'party_preference3', 'party_preference4',
                   'party_preference5', 'party_preference6', 'eligibility', 'participation']

class DemoPage2(Page):
    form_model = Player
    form_fields = ['demonstration_participation_allowed', 'demonstration_participation_notallowed',
                   'demonstration_participation_online', 'social_media']

class DemoPage3(Page):
    form_model = Player
    form_fields = ['household_income', 'general_education', 'ba_location', 'In_welchem_Land_sind_Sie_geboren',
                   'In_welchem_Land_ist_Ihre_Mutter_geboren', 'In_welchem_Land_ist_Ihr_Vater_geboren']

#ballot as a table

class Ballot1(Page):
    form_model = Player
    form_fields = ['ba_ballot1']
    def vars_for_template(self):
        return {'ba_group_assignment': safe_json(self.player.ba_group_assignment)}

#ballot as a picture

class Ballot2(Page):
    form_model = Player
    form_fields = ['ba_ballot_pic1']
    def vars_for_template(self):
        return {'ba_group_assignment': safe_json(self.player.ba_group_assignment)}


# group 0 will get ideology1 page before ballot

class Ideology1(Page):
    form_model = Player
    form_fields = ['ba_positioning', 'ba_party_pos', 'ba_opinion1', 'ba_opinion2', 'ba_opinion3',
                   'ba_opinion4', 'ba_opinion5', 'ba_women1', 'ba_women2', 'ba_women3', 'ba_women4', 'ba_women5',
                   'ba_women6', 'ba_women7', 'ba_women8', 'ba_women9', 'ba_women10', 'ba_men1', 'ba_men2', 'ba_men3',
                   'ba_women4', 'ba_women5', 'ba_men6', 'ba_men7', 'ba_men8', 'ba_men9', 'ba_men10']

    def is_displayed(self):
        return self.player.ba_ideology_assignment == 0
    

# group 1 will get ideology2 page after ballot

class Ideology2(Page):
    form_model = Player
    form_fields = ['ba_positioning', 'ba_party_pos', 'ba_opinion1', 'ba_opinion2', 'ba_opinion3',
                   'ba_opinion4', 'ba_opinion5', 'ba_women1', 'ba_women2', 'ba_women3', 'ba_women4', 'ba_women5',
                   'ba_women6', 'ba_women7', 'ba_women8', 'ba_women9', 'ba_women10', 'ba_men1', 'ba_men2', 'ba_men3',
                   'ba_women4', 'ba_women5', 'ba_men6', 'ba_men7', 'ba_men8', 'ba_men9', 'ba_men10']

    def is_displayed(self):
        return self.player.ba_ideology_assignment == 1


class EndPage(Page):

    form_model = Player

page_sequence = [Welcome,
                DemoPage,
                DemoPage2,
                DemoPage3,
                Ideology1,
                Ballot1,
                Ballot2,
                Ideology2,
                EndPage]
