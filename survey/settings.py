from os import environ


SESSION_CONFIGS = [
    dict(
        name='ballot_survey_test',
        display_name='ballot_survey_test',
        num_demo_participants=10,
        app_sequence=['survey_example_appfolder'],
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True


ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = 'z)#!($1drf8ouid#3qa1edf@q2q=@#y89a!g3vghv5e&bsr^e4'

INSTALLED_APPS = ['otree']
