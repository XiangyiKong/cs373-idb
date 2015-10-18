from app import app
from flask import render_template
from app.marvel_api import get_list_of_characters, get_single_character, get_list_of_comics, get_single_comic

@app.route('/')
def hello_world():
    return render_template('index.html', title='Marvel Database Home', team='swe team')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/splash')
def splash():
    return render_template('splash.html', title='Welcome to marvel', team='swe team')

@app.route('/characters')
def characters():
	character_list = get_list_of_characters()
	return render_template('character_list.html', title='Marvel List of characters', character_list=character_list['data']['results'])

@app.route('/characters/<character_id>')
def single_character(character_id):
	character = get_single_character(character_id)
	return render_template('character.html', title='Character', character=character) #TODO: get title of page from character object/call

@app.route('/comics')
def comics():
	comic_list = get_list_of_comics()
	return render_template('comic_list.html', title='Marvel List of Comics', comic_list=comic_list['data']['results'])

@app.route('/comics/<comic_id>')
def single_comic(comic_id):
	comic = get_single_comic(comic_id)
	return render_template('comic.html', title='Comic', comic=comic) #TODO: get title of page from comic object/call