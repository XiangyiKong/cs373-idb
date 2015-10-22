import hashlib, requests
from local import PRIVATE_KEY
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

def get_list_of_characters(**kwargs):
	query_string = app.config['BASE_URL'] + 'characters' + create_api_params()
	for k,v in kwargs.items():
		query_string += '&' + str(k) + '=' + str(v[0])
	r = requests.get(query_string)
	return r.json()

def get_single_character(character_id):
	query_string = app.config['BASE_URL'] + 'characters/' + str(character_id) + create_api_params()
	r = requests.get(query_string)
	return r.json()

def get_list_of_comics(**kwargs):
	query_string = app.config['BASE_URL'] + 'comics' + create_api_params()
	for k,v in kwargs.items():
		query_string += '&' + str(k) + '=' + str(v[0])
	r = requests.get(query_string)
	return r.json()

def get_single_comic(comic_id):
	query_string = app.config['BASE_URL'] + 'comics/' + str(comic_id) + create_api_params()
	r = requests.get(query_string)
	return r.json()

def get_list_of_creators(**kwargs):
	query_string = app.config['BASE_URL'] + 'creators' + create_api_params()
	for k,v in kwargs.items():
		query_string += '&' + str(k) + '=' + str(v[0])
	r = requests.get(query_string)
	return r.json()

def get_single_creator(creator_id):
	query_string = app.config['BASE_URL'] + 'creators/' + str(creator_id) + create_api_params()
	r = requests.get(query_string)
	return r.json()

def get_list_of_events(**kwargs):
	query_string = app.config['BASE_URL'] + 'events' + create_api_params()
	for k,v in kwargs.items():
		query_string += '&' + str(k) + '=' + str(v[0])
	r = requests.get(query_string)
	return r.json()

def get_single_event(event_id):
	query_string = app.config['BASE_URL'] + 'events/' + str(event_id) + create_api_params()
	r = requests.get(query_string)
	return r.json()

def get_list_of_series(**kwargs):
	query_string = app.config['BASE_URL'] + 'series' + create_api_params()
	for k,v in kwargs.items():
		query_string += '&' + str(k) + '=' + str(v[0])
	r = requests.get(query_string)
	return r.json()

def get_single_series(series_id):
	query_string = app.config['BASE_URL'] + 'series/' + str(series_id) + create_api_params()
	r = requests.get(query_string)
	return r.json()