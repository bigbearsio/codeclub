import unittest
from lib import podcast
import os 

class PodcastTest(unittest.TestCase):
    def test_parse_apple_links(self):
        test_file = (os.path.dirname(__file__) + "/test_data/apple.html")
        htmlContent = open(test_file).read()
        self.assertEqual("https://podcasts.apple.com/th/podcast/ep-17-phoenix/id1485111503?i=1000463727358", podcast._parse_apple_links(htmlContent)[0])

    def test_parse_spotify_links(self):
        test_file = (os.path.dirname(__file__) + "/test_data/spotify.html")
        htmlContent = open(test_file).read()
        self.assertEqual("https://open.spotify.com/episode/3cm0w2ZElG9vHXUsGLCy87", podcast._parse_spotify_links(htmlContent)[0])