from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player

class Welcome(Page):
    form_model = Player


    def before_next_page(self):
        #here we are increasing the counter for each player that goes past the Welcome Page
        self.group.counter += 1

class Ballot1(Page):
    form_model = Player
    form_fields = ['ba_ballot1']

class Ballot2(Page):
    form_model = Player
    form_fields = ['ba_ballot']

class Ballot(Page):
    form_model = Player

class DemoPage(Page):
    form_model = Player
    form_fields = ['please_state_your_age', 'ba_education', 'please_state_your_postal_code', 'ba_gender', 'ba_hidden_input']

class Ideology(Page):
    form_model = Player
    form_fields = ['ba_positioning', 'ba_party_pos']

#change order of ballot page

class EndPage(Page):

    form_model = Player

page_sequence = [Welcome,
                Ballot1,
                Ballot2,
                Ballot,
                DemoPage,
                Ideology,
                EndPage]
