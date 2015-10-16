import hashlib, requests
from app.local import PRIVATE_KEY
from time import time
from flask import current_app as app


def create_api_params():
    '''This function creates a string to use as the parameters when making a call to the 
        Marvel API'''
    epoch = str(int(time()))
    h = hashlib.md5()
    public = '14f4ae6a45f097d65a5b56530da74ecc'
    h.update(epoch.encode('utf-8') + PRIVATE_KEY.encode('utf-8') + public.encode('utf-8'))
    return "?ts=" + epoch + "&apikey=" + public + "&hash=" + h.hexdigest() #string of the parameters for the url call

def get_list_of_characters(name=None, nameStartsWith=None, limit=None, offset=None):
	query_string = app.config['BASE_URL'] + 'characters' + create_api_params()
	if name is not None:
		query_string += '&name=' + name
	if limit is not None:
		query_string += '&limit=' + str(limit)
	r = requests.get(query_string)
	return r.json()