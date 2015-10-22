from app import app
from flask import render_template
from marvel_api import get_list_of_characters, get_single_character, get_list_of_comics, get_single_comic, get_list_of_creators, get_single_creator
import re

@app.route('/')
def splash():
    return render_template('splash.html', title='Welcome to Marvel', team='swe team')

@app.route('/about')
def about():
	return render_template('about.html', title='BitsPlease. We are BitsPlease.')

@app.route('/characters')
def characters():
	character_list = get_list_of_characters()
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
	comic_list = get_list_of_comics()
	return render_template('comic_list.html', title='Marvel List of Comics', comic_list=comic_list['data']['results'])

@app.route('/comics/<comic_id>')
def single_comic(comic_id):
	comic = get_single_comic(comic_id)
	# character_name_list = []
	# for character_url in comic['data']['results'][0]['characters']['items']:
	# 	m = re.match(".+/(?P<character_id>\d+)", character_url['resourceURI'])
	# 	single_character_name = get_single_character(m.group("character_id"))
	# 	character_name_list.append(single_character_name)

	url_list = []
	for comic_url in comic['data']['results'][0]['urls']:
		url_list.append(comic_url)
	# return render_template('comic.html', title=comic['data']['results'][0]['title'], comic=comic, character_name_list=character_name_list, url_list=url_list)
	return render_template('comic.html', title=comic['data']['results'][0]['title'], comic=comic, url_list=url_list) #TODO: get title of page from comic object/call

@app.route('/creators')
def creators():
	creator_list = get_list_of_creators()
	return render_template('creator_list.html', title='Marvel List of creators', creator_list=creator_list['data']['results'])

@app.route('/creators/<creator_id>')
def single_creator(creator_id):
	creator = get_single_creator(creator_id)
	return render_template('creator.html', title=creator['data']['results'][0]['fullName'], creator=creator)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404