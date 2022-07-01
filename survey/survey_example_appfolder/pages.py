from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player

class Welcome(Page):
    form_model = Player

    def before_next_page(self):
        self.group.counter += 1

#ballot as a table

class Ballot1(Page):
    form_model = Player
    form_fields = ['ba_ballot0', 'ba_ballot1', 'ba_ballot2', 'ba_ballot3']

#ballot as a picture

class Ballot2(Page):
    form_model = Player
    form_fields = ['ba_ballot_pic1', 'ba_ballot_pic2', 'ba_ballot_pic3', 'ba_ballot_pic4']

class Ballot(Page):
    form_model = Player

#group 4 will get ideology page before ballot

class Ideology1(Page):
    form_model = Player
    form_fields = ['ba_positioning', 'ba_party_pos']

    def is_displayed(self):
        return self.player.group_assignment == 4

#group 5 will get ideology page after ballot

class Ideology2(Page):
    form_model = Player
    form_fields = ['ba_positioning', 'ba_party_pos']

    def is_displayed(self):
        return self.player.group_assignment == 5

class DemoPage(Page):
    form_model = Player
    form_fields = ['please_state_your_age', 'ba_education', 'please_state_your_postal_code', 'ba_gender', 'ba_hidden_input']

#change order of ballot page

class EndPage(Page):

    form_model = Player

page_sequence = [Welcome,
                Ballot1,
                Ballot2,
                Ideology1,
                Ideology2,
                Ballot,
                DemoPage,
                EndPage]
