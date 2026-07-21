import unittest
from peewee import *
from app import TimelinePost

MODELS=[TimelinePost]

test_db=SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS,False,False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post=TimelinePost.create(name='Baqer',email="baq@gmail.com",content="this is from testdb dude")
        assert first_post.id==1

        second_post=TimelinePost.create(name='amsa',email="asma@gmail.com",content="this is from testdb bube")
        assert second_post.id==2

