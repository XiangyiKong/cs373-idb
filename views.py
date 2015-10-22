from app import app
from flask import render_template, jsonify, request
from marvel_api import (get_list_of_characters, get_single_character, get_list_of_comics, get_single_comic, get_list_of_events,
	get_single_event, get_list_of_series, get_single_series, get_single_creator, get_list_of_creators)
import re

@app.route('/')
def splash():
    return render_template('splash.html', title='Welcome to Marvel', team='swe team')

@app.route('/about')
def about():
	return render_template('about.html', title='BitsPlease. We are BitsPlease.')

@app.route('/characters')
def characters():
	character_list = get_list_of_characters(**request.args)
	return render_template('character_list.html', title='Marvel List of characters', character_list=character_list['data']['results'])

@app.route('/characters/<character_id>')
def single_character(character_id):
	character = get_single_character(character_id)
	comic_name_list = []
	for comic_url in character['data']['results'][0]['comics']['items']:
		m = re.match(".+/(?P<comic_id>\d+)", comic_url['resourceURI'])
		single_comic_name = get_single_comic(m.group("comic_id"))
		comic_name_list.append(single_comic_name)

	url_list = []
	for character_url in character['data']['results'][0]['urls']:
		url_list.append(character_url)
	return render_template('character.html', title=character['data']['results'][0]['name'], character=character, comic_name_list=comic_name_list, url_list=url_list) #TODO: get title of page from character object/call

@app.route('/comics')
def comics():
	comic_list = get_list_of_comics(**request.args)
	return render_template('comic_list.html', title='Marvel List of Comics', comic_list=comic_list['data']['results'])

@app.route('/comics/<comic_id>')
def single_comic(comic_id):
	comic = get_single_comic(comic_id)
	character_name_list = []
	for character_url in comic['data']['results'][0]['characters']['items']:
		m = re.match(".+/(?P<character_id>\d+)", character_url['resourceURI'])
		single_character_name = get_single_character(m.group("character_id"))
		character_name_list.append(single_character_name)

	url_list = []
	for comic_url in comic['data']['results'][0]['urls']:
		url_list.append(comic_url)
	return render_template('comic.html', title=comic['data']['results'][0]['title'], comic=comic, character_name_list=character_name_list, url_list=url_list)

@app.route('/creators')
def creators():
	creator_list = get_list_of_creators(**request.args)
	return render_template('creator_list.html', title='Marvel List of creators', creator_list=creator_list['data']['results'])

@app.route('/creators/<creator_id>')
def single_creator(creator_id):
	creator = get_single_creator(creator_id)
	return render_template('creator.html', title=creator['data']['results'][0]['fullName'], creator=creator)

@app.route('/events')
def events():
	event_list = get_list_of_events(**request.args)
	return render_template('event_list.html', title='Marvel List of Events', event_list=event_list['data']['results'])

@app.route('/events/<event_id>')
def single_event(event_id):
	event = get_single_event(event_id)
	print(event)
	return render_template('event.html', title=event['data']['results'][0]['title'], event=event)

@app.route('/series')
def series():
	series_list = get_list_of_series(**request.args)
	return render_template('series_list.html', title='Marvel List of Series', series_list=series_list['data']['results'])

@app.route('/series/<series_id>')
def single_series(series_id):
	series = get_single_series(series_id)
	return render_template('series.html', title="Title goes here", series=series)

@app.route('/stories')
def stories():
	return render_template('generic.html', title='Coming Soon', content="This will be completed in the next phase of this project. Come back soon!")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/api/characters', methods=['GET'])
def characters_api():
	return jsonify(get_list_of_characters())

@app.route('/api/characters/<character_id>', methods=['GET'])
def single_character_api(character_id):
	return jsonify(get_single_character(character_id))

@app.route('/api/comics', methods=['GET'])
def comics_api():
	return jsonify(get_list_of_comics())

@app.route('/api/comics/<comic_id>', methods=['GET'])
def single_comic_api(comic_id):
	return jsonify(get_single_comic(comic_id))

@app.route('/api/creators', methods=['GET'])
def creators_api():
	return jsonify(get_list_of_creators())

@app.route('/api/creators/<creator_id>', methods=['GET'])
def single_creator_api(creator_id):
	return jsonify(get_single_creator(creator_id))
