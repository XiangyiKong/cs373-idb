import hashlib
from local import PRIVATE_KEY
from time import time


def create_api_params():
    '''This function creates a string to use as the parameters when making a call to the 
        Marvel API'''
    epoch = str(int(time()))
    h = hashlib.md5()
    public = '14f4ae6a45f097d65a5b56530da74ecc'
    h.update(epoch.encode('utf-8') + PRIVATE_KEY.encode('utf-8') + public.encode('utf-8'))
    return "ts=" + epoch + "&apikey=" + public + "&hash=" + h.hexdigest() #string of the parameters for the url call