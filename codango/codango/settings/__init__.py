import os
if not os.getenv('CI') and not os.getenv('HEROKU'):
    from django_envie.workroom import convertfiletovars
    convertfiletovars()
    from development import *
