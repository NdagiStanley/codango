import os
if not os.getenv('CI') and not os.getenv('HEROKU'):
    from development import *
