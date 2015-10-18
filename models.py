from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    thumbnail = db.Column(db.Image)
    resourceURI = db.Column(db.String)
    comics = db.Column()
    stories = db.Column()
    events = db.Column()
    series = db.Column()

    tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('pages', lazy='dynamic'))

class Comics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    issuenumber = db.Column(db.Integer)
    description = db.Column(db.String)
    format = db.Column(db.String)
    pagecount = db.Column(db.Integer)
    resourceURI = db.Column(db.String)
    series = db.Column() ################
    thumbnail = db.Column(db.Image)
    images = db.Column() ################
    creators = db.Column()
    characters = db.Column()
    stories = db.Column()
    events = db.Column()

