from os import environ

SESSION_CONFIGS = [
        dict(
                name='stage_1_instructions',
                display_name="Stage 1: Instructions",
                num_demo_participants=2,
                app_sequence=['STG1_1']
        ),
        dict(
                name='stage_1_game',
                display_name="Stage 1: Game",
                num_demo_participants=2,
                app_sequence=['STG1_2']
        ),
        dict(
                name='stage 1',
                display_name="Stage 1: Full Demo",
                num_demo_participants=2,
                app_sequence=['STG1_BGN']
        ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
        real_world_currency_per_point=1, participation_fee=0.00, doc=""
)


PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '7890095873655'
