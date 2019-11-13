import os
import unittest

 
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
print(THIS_DIR.rsplit('\\',1)[0])
 
import sys
sys.path.append(THIS_DIR.rsplit('\\',1)[0])
from main import app
from tools import fusionImages, query_api
from PIL import Image

 
class ResultTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
 
        
 
    # executed after each test
    def tearDown(self):
        pass
 
 
###############
#### tests ####
###############
 
    def test_fusionImages_width(self):
        latitude="41.85"
        longitude="-87.65"
        query_api(latitude,longitude,"tests/img.png")
        
        response=fusionImages("tests/img.png","tests/plume.png","tests/fusioned.png")
        self.assertEqual(response.width, 514)
        
    def test_fusionImages_height(self):
        latitude="41.85"
        longitude="-87.65"
        query_api(latitude,longitude,"tests/img.png")
        response=fusionImages("tests/img.png","tests/plume.png","tests/fusioned.png")
        self.assertEqual(response.height, 257)

    def test_fusionImages_noError(self):
        latitude="41.85"
        longitude="-87.65"
        try:
             query_api(latitude,longitude,"tests/img.png")
             response=fusionImages("tests/img.png","tests/plume.png","tests/fusioned.png")
        except Exception:
             self.fail("Errors detected")
    
 
if __name__ == "__main__":
    unittest.main()
