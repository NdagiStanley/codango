import os
if not os.getenv('CI'):
    from development import *
