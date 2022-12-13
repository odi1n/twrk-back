from .base import *

if env.str('ENVIRONMENT') == 'production':
    from .production import *
else:
    from .development import *
