import unittest
import os

os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

        html = resp.get_data(as_text=True)
        self.assertIn("<title>Baker Hassani</title>", html)

        #add more tests relating to home page -- implementation notes:
        #there isn't much to test (static page) so checked linked pages are returning ok
        #if the other pages get hooked in they would need to be tested too, 
        #they are not currently linked on the home page though, that is using scroll handles
        self.assertEqual(self.client.get("/education").status_code, 200)
        self.assertEqual(self.client.get("/timeline").status_code, 200)


    def test_timeline(self):
        resp = self.client.get("/api/timeline_post")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.headers.get('Content-Type'), 'application/json')

        json = resp.get_json()
        self.assertIn("timeline_posts", json)
        self.assertEqual(len(json["timeline_posts"]), 0)

        #add more tests relating to the /api/timeline_post GET and POST apis

        #send post and check ok and has expected content
        resp = self.client.post("/api/timeline_post", data={'name': 'John Doe', 'email': 'john@example.com', 'content': 'Hello world, I\'m John!'})
        self.assertEqual(resp.status_code, 200)

        post = resp.get_json()
        post = (post['name'], post['email'], post['content'])
        self.assertEqual(post, ('John Doe', 'john@example.com', "Hello world, I'm John!"))

        #get posts from api and check there is only 1 and has expected content
        resp = self.client.get("/api/timeline_post")
        posts = resp.get_json()['timeline_posts']
        self.assertEqual(len(posts), 1)

        actualPost = (posts[0]['name'], posts[0]['email'], posts[0]['content'])
        self.assertEqual(actualPost, post)

        #add more tests relating to the timeline page
        #similar to home page, not much to test as the page is mainly js
        resp = self.client.get("/timeline")
        self.assertEqual(resp.status_code, 200)

        #can't test because js injection - but posts are rendering the wrong way
        #NOTE: fix timeline render order (posts.reverse() in timeline.html script)

    def test_malformed_timeline_post(self):
        #POST req missing name
        resp = self.client.post("/api/timeline_post", data={'email': 'john@example.com', 'content': 'Hello world, I\'m John!'})
        self.assertEqual(resp.status_code, 400)

        html = resp.get_data(as_text=True)
        self.assertIn("Invalid Name", html)

        #POST req with empty content
        resp = self.client.post("/api/timeline_post", data={'name': 'John Doe', 'email': 'john@example.com', 'content': ''})
        self.assertEqual(resp.status_code, 400)

        html = resp.get_data(as_text=True)
        self.assertIn("Invalid Content", html)
        
        #POST req with malformed email
        resp = self.client.post("/api/timeline_post", data={'name': 'John Doe', 'email': 'not-an-email', 'content': 'Hello world, I\'m John!'})
        self.assertEqual(resp.status_code, 400)

        html = resp.get_data(as_text=True)
        self.assertIn("Invalid Email", html)