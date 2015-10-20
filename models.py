from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#################
# relationships #
#################

# many-to-many between characters and comics
characters_comics_association = Table('characters_comics', Base.metadata,
    Column('characters_id', Integer, ForeignKey('characters.id')),
    Column('comics_id', Integer, ForeignKey('comics.id'))
)

# many-to-many between characters and stories
characters_stories_association = Table('characters_stories', Base.metadata,
    Column('characters_id', Integer, ForeignKey('characters.id')),
    Column('stories_id', Integer, ForeignKey('stories.id'))
)

# many-to-many between characters and events
characters_events_association = Table('characters_events', Base.metadata,
    Column('characters_id', Integer, ForeignKey('characters.id')),
    Column('events_id', Integer, ForeignKey('events.id'))
)

# many-to-many between characters and series
characters_series_association = Table('characters_series', Base.metadata,
    Column('characters_id', Integer, ForeignKey('characters.id')),
    Column('series_id', Integer, ForeignKey('series.id'))
)

# many-to-many between comics and creators
comics_creators_association = Table('comics_creators', Base.metadata,
    Column('comics_id', Integer, ForeignKey('comics.id')),
    Column('creators_id', Integer, ForeignKey('creators.id'))
)

# many-to-many between comics and stories
comics_stories_association = Table('comics_stories', Base.metadata,
    Column('comics_id', Integer, ForeignKey('comics.id')),
    Column('stories_id', Integer, ForeignKey('stories.id'))
)

# many-to-many between comics and events
comics_events_association = Table('comics_events', Base.metadata,
    Column('comics_id', Integer, ForeignKey('comics.id')),
    Column('events_id', Integer, ForeignKey('events.id'))
)

# many-to-many between creators and series
creators_series_association = Table('creators_series', Base.metadata,
    Column('creators_id', Integer, ForeignKey('creators.id')),
    Column('series_id', Integer, ForeignKey('series.id'))
)

# many-to-many between creators and stories
creators_stories_association = Table('creators_stories', Base.metadata,
    Column('creators_id', Integer, ForeignKey('creators.id')),
    Column('stories_id', Integer, ForeignKey('stories.id'))
)

# many-to-many between creators and events
creators_events_association = Table('creators_events', Base.metadata,
    Column('creators_id', Integer, ForeignKey('creators.id')),
    Column('events_id', Integer, ForeignKey('events.id'))
)

# many-to-many between events and series
events_series_association = Table('events_series', Base.metadata,
    Column('events_id', Integer, ForeignKey('events.id')),
    Column('series_id', Integer, ForeignKey('series.id'))
)

# many-to-many between events and creators
events_creators_association = Table('events_creators', Base.metadata,
    Column('events_id', Integer, ForeignKey('events.id')),
    Column('creators_id', Integer, ForeignKey('creators.id'))
)

# many-to-many between seriess and stories
series_stories_association = Table('series_stories', Base.metadata,
    Column('series_id', Integer, ForeignKey('series.id')),
    Column('stories_id', Integer, ForeignKey('stories.id'))
)


##########
# models #
##########

####################
# characters model #
####################

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    thumbnail = Column(Image)
    url = Column(String)

    comics = relationship("Comics",
                secondary = characters_comics_association,
                backref = "characters")

    stories = relationship("Stories",
                secondary = characters_stories_association,
                backref = "characters")

    events = relationship("Events",
                secondary = characters_events_association,
                backref = "characters")

    series = relationship("Series",
                secondary = characters_series_association,
                backref = "characters")

################
# comics model #
################

class Comics(Base):
    __tablename__ = 'comics'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    issuenumber = Column(Integer)
    description = Column(String)
    format = Column(String)
    pageCount = Column(Integer)
    url = Column(String)
    series = Column(Integer, ForeignKey('series.id')) # one-to-many
    thumbnail = Column(Image)
    images = relationship("Images")
    creators = relationship("Creators",
                secondary = comics_creators_association,
                backref = "comics")
    stories = relationship("Stories",
                secondary = comics_stories_association,
                backref = "comics")
    events = relationship("Events",
                secondary = comics_events_association,
                backref = "comics")

# table for images in a comic
class Images(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    comics_id = Column(Integer, ForeignKey('comics.id'))
    path = Column(String)

##################
# creators model #
##################

class Creators(Base):
    __tablename__ = 'creators'
    id = Column(Integer, primary_key=True)
    fullName = Column(String)
    url = Column(String)
    thumbnail = Column(Image)
    series = relationship("Series",
                secondary = creators_series_association,
                backref = "creators")
    stories = relationship("Stories",
                secondary = creators_stories_association,
                backref = "creators")
    events = relationship("Events",
                secondary = creators_events_association,
                backref = "creators")

################
# events model #
################

class Events(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    url = Column(String)
    start = Column(Date)
    end = Column(Date)
    thumbnail = Column(Image)
    series = relationship("Series",
                secondary = events_series_association,
                backref = "events")

    creators = relationship("Creators",
                secondary = events_creators_association,
                backref = "events")
    next = Column(String)
    previous = Column(String)

################
# series model #
################

class Series(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    url = Column(String)
    startYear = Column(Integer)
    endYear = Column(Integer)
    rating = Column(String)
    thumbnail = Column(Image)
    comics = relationship("Comics", backref="series")
    stories = relationship("Stories",
                secondary = series_stories_association,
                backref = "series")
    next = Column(String)
    previous = Column(String)

#################
# stories model #
#################

class Stories(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    storyType = Column(String)
    thumbnail = Column(Image)
    originalIssue = Column(String)