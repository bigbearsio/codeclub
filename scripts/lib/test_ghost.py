import unittest
from lib import ghost
import os 

class Ghost(unittest.TestCase):
    def test_get_latest_episode_from_content(self):
        test_file = (os.path.dirname(__file__) + "/test_data/rss.xml")
        xmlContent = open(test_file).read()
        self.assertEqual(16, ghost.get_latest_episode_from_content(xmlContent))