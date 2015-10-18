from local import SECRET_KEY

WTF_CSRF_ENABLED = True
WTF_CSRF_METHODS = ['DELETE']
BASE_URL = "http://gateway.marvel.com/v1/public/"