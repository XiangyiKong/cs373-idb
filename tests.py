#!/usr/bin/env python3

# -------
# imports
# -------

import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Characters, Comics, Creators, Events, Series, 
    Stories, Images)

# -----------
# TestModels
# -----------

class TestModels (TestCase) :

    ############
    # Database #
    ############

    def setUp(self):
        self.engine = create_engine('mysql+pymysql://')
        self.session = Session(engine)
        Base.metadata.create_all(self.engine)

        self.characters_instance = Characters(1009610, 
                                              "Spider-Man", 
                                              None,
                                              None,
                                              None,
                                              None,
                                              None,
                                              None,
                                              None)
        self.session.add(self.character_instance)

        self.comics_instance = Comics(1, 'ion torrent', 'start')
        self.session.add(self.comics_instance)

        self.creators_instance = Creators(1, 'ion torrent', 'start')
        self.session.add(self.creators_instance)

        self.events_instance = Events(1, 'ion torrent', 'start')
        self.session.add(self.events_instance)

        self.series_instance = Series(1, 'ion torrent', 'start')
        self.session.add(self.series_instance)

        self.stories_instance = Stories(1, 'ion torrent', 'start')
        self.session.add(self.stories_instance)

        self.images_instance = Images(1, 'ion torrent', 'start')
        self.session.add(self.images_instance)


        self.session.commit()

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    ##########
    # Models #
    ##########

    # ----------
    # Characters
    # ----------

    def test_query_characters(self):
        expected = [self.characters]
        result = self.session.query(Characters).all()
        self.assertEqual(result, expected)

    def test_constructor_characters(self):
        self.assertEqual(self.characters_instance.id, 1009610)
        self.assertEqual(self.characters_instance.name, "Spider-Man")

    def test_delete_characters(self):
        expected = [self.characters]
        result = self.session.query(Characters).all()
        self.assertEqual(result, expected)

    # ------
    # Comics
    # ------

    def test_query_comics(self):
        expected = [self.comics]
        result = self.session.query(Comics).all()
        self.assertEqual(result, expected)

    def test_constructor_comics(self):
        self.assertEqual(self.comics_instance.name, 'SomeName')
        self.assertEqual(self.comics_instance.data, 'some data')

    # --------
    # Creators
    # --------

    def test_query_creators(self):
        expected = [self.creators]
        result = self.session.query(Creators).all()
        self.assertEqual(result, expected)

    def test_constructor_creators(self):
        self.assertEqual(self.creators_instance.name, 'SomeName')
        self.assertEqual(self.creators_instance.data, 'some data')


    # ------
    # Events
    # ------

    def test_query_events(self):
        expected = [self.events]
        result = self.session.query(Events).all()
        self.assertEqual(result, expected)

    def test_constructor_events(self):
        self.assertEqual(self.events_instance.name, 'SomeName')
        self.assertEqual(self.events_instance.data, 'some data')

    # ------
    # Series
    # ------

    def test_query_series(self):
        expected = [self.series]
        result = self.session.query(Series).all()
        self.assertEqual(result, expected)

    def test_constructor_series(self):
        self.assertEqual(self.series_instance.name, 'SomeName')
        self.assertEqual(self.series_instance.data, 'some data')

    # -------
    # Stories
    # -------

    def test_query_stories(self):
        expected = [self.stories]
        result = self.session.query(Stories).all()
        self.assertEqual(result, expected)

    def test_constructor_stories(self):
        self.assertEqual(self.stories_instance.name, 'SomeName')
        self.assertEqual(self.stories_instance.data, 'some data')


    # ------
    # Images
    # ------

    def test_query_images(self):
        expected = [self.images]
        result = self.session.query(Images).all()
        self.assertEqual(result, expected)

    def test_constructor_images(self):
        self.assertEqual(self.images_instance.name, 'SomeName')
        self.assertEqual(self.images_instance.data, 'some data')

# ----
# main
# ----

if __name__ == "__main__" :
    main()