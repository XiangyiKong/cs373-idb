from app import app
from flask import render_template, jsonify, request
from marvel_api import (get_list_of_characters, get_single_character, get_list_of_comics, get_list_of_events,
	get_single_event, get_list_of_series, get_single_series, get_single_comic, get_list_of_creators, get_single_creator)
from git_api import get_contributor_list
import re

@app.route('/')
def splash():
    return render_template('splash.html', title='Welcome to Marvel', team='swe team')

@app.route('/about')
def about():
	return render_template('about.html', title='BitsPlease. We are BitsPlease.', contributor_list=get_contributor_list())

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
	comic_name_list = []
	for comic_url in event['data']['results'][0]['comics']['items']:
		m = re.match(".+/(?P<comic_id>\d+)", comic_url['resourceURI'])
		single_comic_name = get_single_comic(m.group("comic_id"))
		comic_name_list.append(single_comic_name)

	character_name_list = []
	# for character_url in event['data']['results'][0]['characters']:
	# 	m = re.match(".+/(?P<character_id>\d+)", character_url['resourceURI'])
	# 	single_character_name = get_single_character(m.group("character_id"))
	# 	print "#####################"
	# 	print m.group("character_id")
	# 	character_name_list.append(single_character_name)

	creator_name_list=[]
	for creator_url in event['data']['results'][0]['creators']['items']:
		m = re.match(".+/(?P<creator_id>\d+)", creator_url['resourceURI'])
		single_creator_name = get_single_creator(m.group("creator_id"))
		creator_name_list.append(single_creator_name)
	return render_template('event.html', title=event['data']['results'][0]['title'], event=event, comic_name_list=comic_name_list, character_name_list=character_name_list, creator_name_list=creator_name_list)

@app.route('/series')
def series():
	series_list = get_list_of_series(**request.args)
	return render_template('series_list.html', title='Marvel List of Series', series_list=series_list['data']['results'])

@app.route('/series/<series_id>')
def single_series(series_id):
	series = get_single_series(series_id)
	character_name_list = []
	for character_url in series['data']['results'][0]['characters']['items']:
		m = re.match(".+/(?P<character_id>\d+)", character_url['resourceURI'])
		single_character_name = get_single_character(m.group("character_id"))
		character_name_list.append(single_character_name)

	comic_name_list = []
	for comic_url in series['data']['results'][0]['comics']['items']:
		m = re.match(".+/(?P<comic_id>\d+)", comic_url['resourceURI'])
		single_comic_name = get_single_comic(m.group("comic_id"))
		comic_name_list.append(single_comic_name)

	creator_name_list = []
	for creator_url in series['data']['results'][0]['creators']['items']:
		m = re.match(".+/(?P<creator_id>\d+)", creator_url['resourceURI'])
		single_creator_name = get_single_creator(m.group("creator_id"))
		creator_name_list.append(single_creator_name)

	event_name_list = []
	for event_url in series['data']['results'][0]['events']['items']:
		m = re.match(".+/(?P<event_id>\d+)", event_url['resourceURI'])
		single_event_name = get_single_event(m.group("event_id"))
		event_name_list.append(single_event_name)

	# story_name_list = []
	# for story_url in series['data']['results'][0]['stories']['items']:
	# 	m = re.match(".+/(?P<story_id>\d+)", story_url['resourceURI'])
	# 	single_story_name = get_single_story(m.group("story_id"))
	# 	creator_story_list.append(single_story_name)

	url_list = []
	for series_url in series['data']['results'][0]['urls']:
		url_list.append(series_url)
	return render_template('series.html', title="Title goes here", series=series, character_name_list=character_name_list, comic_name_list=comic_name_list, creator_name_list=creator_name_list, event_name_list=event_name_list, url_list=url_list)

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
