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
    url = db.Column(db.String)
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
    pageCount = db.Column(db.Integer)
    url = db.Column(db.String)
    series = db.Column() ################
    thumbnail = db.Column(db.Image)
    images = db.Column() ################
    creators = db.Column()
    characters = db.Column()
    stories = db.Column()
    events = db.Column()

class Creators(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String)
    url = db.Column(db.String)
    thumbnail = db.Column(db.Image)
    series = db.Column()
    stories = db.Column()
    comics = db.Column()
    events = db.Column()

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    url = db.Column(db.String)
    start = db.Column(db.Date)
    end = db.Column(db.Date)
    thumbnail = db.Column(db.Image)
    comics = db.Column()
    stories = db.Column()
    series = db.Column()
    characters = db.Column()
    creators = db.Column()
    next = db.Column(db.String)
    previous = db.Column(db.String)

class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    url = db.Column(db.String)
    startYear = db.Column(db.Integer)
    endYear = db.Column(db.Integer)
    rating = db.Column(db.String)
    thumbnail = db.Column(db.Image)
    comics = db.Column()
    stories = db.Column()
    events = db.Column()
    characters = db.Column()
    creators = db.Column()
    next = db.Column(db.String)
    previous = db.Column(db.String)

class Stories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    storyType = db.Column(db.String)
    thumbnail = db.Column(db.Image)
    comics = db.Column()
    series = db.Column()
    events = db.Column()
    characters = db.Column()
    creators = db.Column()
    originalIssue = db.Column(db.String)