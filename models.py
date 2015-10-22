from sqlalchemy import (Table, Column, Integer, Date, String, ForeignKey, 
    create_engine, MetaData)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#################
# relationships #
#################

# many-to-many characters<->comics
characters_comics_association = Table('characters_comics', Base.metadata,
    Column('characters_id', Integer, ForeignKey('characters.id')),
    Column('comics_id', Integer, ForeignKey('comics.id'))
)

# many-to-many characters<->stories
characters_stories_association = Table('characters_stories', Base.metadata,
    Column('characters_id', Integer, ForeignKey('characters.id')),
    Column('stories_id', Integer, ForeignKey('stories.id'))
)

# many-to-many characters<->events
characters_events_association = Table('characters_events', Base.metadata,
    Column('characters_id', Integer, ForeignKey('characters.id')),
    Column('events_id', Integer, ForeignKey('events.id'))
)

# many-to-many characters<->series
characters_series_association = Table('characters_series', Base.metadata,
    Column('characters_id', Integer, ForeignKey('characters.id')),
    Column('series_id', Integer, ForeignKey('series.id'))
)

# many-to-many comics<->creators
comics_creators_association = Table('comics_creators', Base.metadata,
    Column('comics_id', Integer, ForeignKey('comics.id')),
    Column('creators_id', Integer, ForeignKey('creators.id'))
)

# many-to-many comics<->stories
comics_stories_association = Table('comics_stories', Base.metadata,
    Column('comics_id', Integer, ForeignKey('comics.id')),
    Column('stories_id', Integer, ForeignKey('stories.id'))
)

# many-to-many comics<->events
comics_events_association = Table('comics_events', Base.metadata,
    Column('comics_id', Integer, ForeignKey('comics.id')),
    Column('events_id', Integer, ForeignKey('events.id'))
)

# many-to-many creators<->series
creators_series_association = Table('creators_series', Base.metadata,
    Column('creators_id', Integer, ForeignKey('creators.id')),
    Column('series_id', Integer, ForeignKey('series.id'))
)

# many-to-many creators<->stories
creators_stories_association = Table('creators_stories', Base.metadata,
    Column('creators_id', Integer, ForeignKey('creators.id')),
    Column('stories_id', Integer, ForeignKey('stories.id'))
)

# many-to-many creators<->events
creators_events_association = Table('creators_events', Base.metadata,
    Column('creators_id', Integer, ForeignKey('creators.id')),
    Column('events_id', Integer, ForeignKey('events.id'))
)

# many-to-many events<->series
events_series_association = Table('events_series', Base.metadata,
    Column('events_id', Integer, ForeignKey('events.id')),
    Column('series_id', Integer, ForeignKey('series.id'))
)

# many-to-many events<->creators
events_creators_association = Table('events_creators', Base.metadata,
    Column('events_id', Integer, ForeignKey('events.id')),
    Column('creators_id', Integer, ForeignKey('creators.id'))
)

# many-to-many seriess<->stories
series_stories_association = Table('series_stories', Base.metadata,
    Column('series_id', Integer, ForeignKey('series.id')),
    Column('stories_id', Integer, ForeignKey('stories.id'))
)

# table for images in a comic
class Images(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    comics_id = Column(Integer, ForeignKey('comics.id'))
    path = Column(String)

##########
# models #
##########

class Characters(Base):
    """ A model to represent heroes and villians who appear in a Marvel comic

    Attributes:
        id: An integer representing the unique ID of the character
        name: A string representing the name of the character
        description: A string indicating a short bio of the character
        thumbnail: An image of the character
        url: A string representing the URL indentifier for this character
        comics: A list containing comics which feature this character
        stories: A list containing stories in which this character appears
        events: A list containing events in which this character appears
        series: A list containing series in which this character appears
    """
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    thumbnail = Column(Integer, ForeignKey('images.id'))
    url = Column(String)
    comics = relationship("Comics",
                secondary =lambda: characters_comics_association,
                backref = "characters")
    stories = relationship("Stories",
                secondary =lambda: characters_stories_association,
                backref = "characters")
    events = relationship("Events",
                secondary =lambda: characters_events_association,
                backref = "characters")
    series = relationship("Series",
                secondary =lambda: characters_series_association,
                backref = "characters")

class Comics(Base):
    """ A model to represent a Marvel comic

    Attributes:
        id: An integer representing the unique ID of the comic
        title: A string representing the title of the comic
        issueNumber: An integer for the number of the issue in the series 
        description: A string describing the comic
        format: A string indicating the publication format of the comic
        pageCount: An integer for the number of story pages in the comic
        url: A string representing the URL indentifier for this comic
        series: An integer representing a foreing key to its series 
        thumbnail: An image of the character
        images: A list of promotional images associated with this comic
        creators: A list containing the creators associated with this comic
        characters: A list containing the characters which appear in this comic
        stories: A list containing the stories which appear in this comic
        events: A listcontaining the events in which this comic appears
    """
    __tablename__ = 'comics'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    issueNumber = Column(Integer)
    description = Column(String)
    format = Column(String)
    pageCount = Column(Integer)
    url = Column(String)
    # one-to-many series<->comics
    series = Column(Integer, ForeignKey('series.id')) 
    thumbnail = Column(Integer, ForeignKey('images.id'))
    images = relationship("Images")
    creators = relationship("Creators",
                secondary =lambda: comics_creators_association,
                backref = "comics")
    stories = relationship("Stories",
                secondary =lambda: comics_stories_association,
                backref = "comics")
    events = relationship("Events",
                secondary =lambda: comics_events_association,
                backref = "comics")

class Creators(Base):
    """ A model to people and entities that make Marvel comics

    Attributes:
        id: An integer representing the unique ID of the creator
        fullName: A string representing the name of the creator
        url: A string representing the URL indentifier for this creator
        thumbnail: An image of the creator
        series: A list containing the series which feature work by this creator
        stories: A list containing the stories which feature work by this creator
        comics: A list containing the comics which feature work by this creator
        events: A list containing the events which feature work by this creator
    """
    __tablename__ = 'creators'
    id = Column(Integer, primary_key=True)
    fullName = Column(String)
    url = Column(String)
    thumbnail = Column(Integer, ForeignKey('images.id'))
    series = relationship("Series",
                secondary =lambda: creators_series_association,
                backref = "creators")
    stories = relationship("Stories",
                secondary =lambda: creators_stories_association,
                backref = "creators")
    events = relationship("Events",
                secondary =lambda: creators_events_association,
                backref = "creators")

class Events(Base):
    """ A model that describes an universe-changing storyline

    Attributes:
        id: An integer representing the unique ID of the event
        title: A string representing the title of the event
        description: A string for the description of the event
        url: A string representing the URL indentifier for this event
        start: The date of publication of the first issue in this event
        end: The date of publication of the last issue in this event
        thumbnail: An image of the event
        comics: A list containing the comics in this event
        stories: A list containing the stories in this event
        series: A list containing the series in this event
        characters: A list containing the characters which appear in this event
        creators: A list containing creators whose work appears in this event
        next: A string describing the event which follows this event
        previous: A string describing the event which preceded this event
    """
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    url = Column(String)
    start = Column(Date)
    end = Column(Date)
    thumbnail = Column(Integer, ForeignKey('images.id'))
    series = relationship("Series",
                secondary =lambda: events_series_association,
                backref = "events")
    creators = relationship("Creators",
                secondary =lambda: events_creators_association,
                backref = "events")
    next = Column(String)
    previous = Column(String)

class Series(Base):
    """ A model to represent a sequentially number list 
    of comics with the same title and volume

    Attributes:
        id: An integer representing the unique ID of the series
        title: A string representing the canonical title of the series
        description: A string for the description of the series
        url: A string representing the URL indentifier for this series
        startYear: An integer for the first year of publication for the series
        endYear: An integer for the last year of publication for the series
        rating: An integer representing the rating for the series
        thumbnail: An image of the series
        comics: A list containing comics in this series
        stories: A list containing stories which occur in comics in this series
        events: A list  containing events which take place in comics in this series
        characters: A list containing characters which appear in comics in this series
        creators: A list of creators whose work appears in comics in this series
        next: A string describing the series which follows this series
        previous: A string describing the series which preceded this series
    """
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    url = Column(String)
    startYear = Column(Integer)
    endYear = Column(Integer)
    rating = Column(String)
    thumbnail = Column(Integer, ForeignKey('images.id'))
    comics = relationship("Comics", backref="series")
    stories = relationship("Stories",
                secondary =lambda: series_stories_association,
                backref = "series")
    next = Column(String)
    previous = Column(String)

class Stories(Base):
    """ A model to represent indivisible components of Marvel comics

    Attributes:
        id: An integer representing the unique ID of the stories
        title: A string representing the story title
        description: A string representing short description of the story
        storyType: A string representing the story type
        thumbnail: An image of the series
        comics: A list containing comics in which this story takes place
        series: A list containing series in which this story appears
        events: A list of the events in which this story appears
        characters: A list of characters which appear in this story
        creators: A list of creators who worked on this story
        originalIssue: A string for the issue in which this story was originally published
    """
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    storyType = Column(String)
    thumbnail = Column(Integer, ForeignKey('images.id'))
    originalIssue = Column(String)

if __name__ == '__main__':
    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)
