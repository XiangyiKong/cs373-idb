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
                                              "Spider-Man")
        self.session.add(self.character_instance)

        self.comics_instance = Comics(30885, 
                                      "Age of Heroes (Trade Paperback)")
        self.session.add(self.comics_instance)

        self.creators_instance = Creators(9799, 
                                          "David Baldeon")
        self.session.add(self.creators_instance)

        self.events_instance = Events(116, 
                                      "Acts of Vengeance!")
        self.session.add(self.events_instance)

        self.series_instance = Series(10235, 
                                      "Age of Heroes (2011)")
        self.session.add(self.series_instance)

        self.stories_instance = Stories(483, 
                                      "Interior #483")
        self.session.add(self.stories_instance)

        self.images_instance = Images(1, 
                                      0,
                                      "http://i.annihil.us/u/prod/marvel/i/mg/3/40/4c06c8261544e")
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
        self.session.query.filter_by(id=1009610).delete()
        characters = self.session.query(Characters).all()
        self.assertNotIn(self.characters_instance, characters)

    # ------
    # Comics
    # ------

    def test_query_comics(self):
        expected = [self.comics]
        result = self.session.query(Comics).all()
        self.assertEqual(result, expected)

    def test_constructor_comics(self):
        self.assertEqual(self.comics_instance.id, 30885)
        self.assertEqual(self.comics_instance.title, "Age of Heroes (Trade Paperback)")

    def test_delete_comics(self):
        self.session.query.filter_by(id=30885).delete()
        comics = self.session.query(Comics).all()
        self.assertNotIn(self.comics_instance, comics)


    # --------
    # Creators
    # --------

    def test_query_creators(self):
        expected = [self.creators]
        result = self.session.query(Creators).all()
        self.assertEqual(result, expected)

    def test_constructor_creators(self):
        self.assertEqual(self.creators_instance.id, 9799)
        self.assertEqual(self.creators_instance.fullName, "David Baldeon")

    def test_delete_creators(self):
        self.session.query.filter_by(id=9799).delete()
        creators = self.session.query(Creators).all()
        self.assertNotIn(self.creators_instance, creators)

    # ------
    # Events
    # ------

    def test_query_events(self):
        expected = [self.events]
        result = self.session.query(Events).all()
        self.assertEqual(result, expected)

    def test_constructor_events(self):
        self.assertEqual(self.events_instance.id, 116)
        self.assertEqual(self.events_instance.title, "Acts of Vengeance!")

    def test_delete_events(self):
        self.session.query.filter_by(id=116).delete()
        events = self.session.query(Events).all()
        self.assertNotIn(self.events_instance, events)

    # ------
    # Series
    # ------

    def test_query_series(self):
        expected = [self.series]
        result = self.session.query(Series).all()
        self.assertEqual(result, expected)

    def test_constructor_series(self):
        self.assertEqual(self.series_instance.name, 10235)
        self.assertEqual(self.series_instance.title, "Age of Heroes (2011)")

    def test_delete_series(self):
        self.session.query.filter_by(id=10235).delete()
        series = self.session.query(Series).all()
        self.assertNotIn(self.series_instance, series)

    # -------
    # Stories
    # -------

    def test_query_stories(self):
        expected = [self.stories]
        result = self.session.query(Stories).all()
        self.assertEqual(result, expected)

    def test_constructor_stories(self):
        self.assertEqual(self.stories_instance.id, 483)
        self.assertEqual(self.stories_instance.title, "Interior #483")

    def test_delete_stories(self):
        self.session.query.filter_by(id=483).delete()
        stories = self.session.query(Stories).all()
        self.assertNotIn(self.stories_instance, stories)


    # ------
    # Images
    # ------

    def test_query_images(self):
        expected = [self.images]
        result = self.session.query(Images).all()
        self.assertEqual(result, expected)

    def test_constructor_images(self):
        self.assertEqual(self.images_instance.id, 1)
        self.assertEqual(self.images_instance.path, 
            "http://i.annihil.us/u/prod/marvel/i/mg/3/40/4c06c8261544e")

    def test_delete_images(self):
        self.session.query.filter_by(id=1).delete()
        images = self.session.query(Images).all()
        self.assertNotIn(self.images_instance, images)

# ----
# main
# ----

if __name__ == "__main__" :
    main()