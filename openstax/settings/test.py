from .base import *

DEBUG = True

###########################################
#        OPENSTAX ACCOUNTS SETTINGS       #
###########################################
AUTHORIZATION_URL = 'https://accounts-qa.openstax.org/oauth/authorize'
ACCESS_TOKEN_URL = 'https://accounts-qa.openstax.org/oauth/token'
USER_QUERY = 'https://accounts-qa.openstax.org/api/user?'

SOCIAL_AUTH_OPENSTAX_KEY = '0a3c6b8c21091873805181b4b2a42cdbabeec6f6871332b817f59fac37033537'
SOCIAL_AUTH_OPENSTAX_SECRET = '40035a7f2a7948b33ffce370af3918d692b958a6cc195e8b57b1fbe621a88157'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'http://os-webview-dev.openstax.org'
SOCIAL_AUTH_SANITIZE_REDIRECTS = False

try:
    from .local import *
except ImportError:
    pass

