from app import app
from flask import render_template
from app.marvel_api import get_list_of_characters

@app.route('/')
def hello_world():
    return render_template('index.html', title='Marvel Database Home', team='swe team')

@app.route('/characters')
def characters():
	character_list = get_list_of_characters()
	return render_template('character_list.html', title='Marvel List of characters', character_list=character_list['data']['results'])

@app.route('/characters/<character_id>')
def characters():
	return render_template('character.html', title='Characters')
