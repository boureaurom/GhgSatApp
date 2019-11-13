import os
import unittest

 
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
print(THIS_DIR.rsplit('\\',1)[0])
 
import sys
sys.path.append(THIS_DIR.rsplit('\\',1)[0])
from main import app
from tools import query_api
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
 
    def test_query_api_width(self):
        latitude="41.85"
        longitude="-87.65"
        query_api(latitude,longitude,"tests/img.png")
        response=Image.open("tests/img.png")
        self.assertEqual(response.width, 514)
        
    def test_query_api_height(self):
        latitude="41.85"
        longitude="-87.65"
        query_api(latitude,longitude,"tests/img.png")
        response=Image.open("tests/img.png")
        self.assertEqual(response.height, 257)

    def test_query_api_noError(self):
        latitude="41.85"
        longitude="-87.65"
        try:
             query_api(latitude,longitude,"tests/img.png")
        except Exception:
             self.fail("Errors detected")
    def test_query_api_error_latitude(self):
        latitude="200"
        longitude="-87.65"
        self.assertRaises(Exception, query_api(latitude,longitude,"tests/img.png"))
    def test_query_api_error_longitude(self):
        latitude="41.85"
        longitude="-200"
        self.assertRaises(Exception, query_api(latitude,longitude,"tests/img.png"))
    def test_query_api_error_emptyString_latitude(self):
        latitude=""
        longitude="-87.65"
        self.assertRaises(Exception, query_api(latitude,longitude,"tests/img.png"))
    def test_query_api_error_emptyString_longitude(self):
        latitude="41.85"
        longitude=""
        self.assertRaises(Exception, query_api(latitude,longitude,"tests/img.png"))
    def test_query_api_error_tooLongString_latitude(self):
        latitude="41.8599999"
        longitude="-87.65"
        self.assertRaises(Exception, query_api(latitude,longitude,"tests/img.png"))
    def test_query_api_error_tooLongString_longitude(self):
        latitude="41.85"
        longitude="-87.6599999"
        self.assertRaises(Exception, query_api(latitude,longitude,"tests/img.png"))
     
 
if __name__ == "__main__":
    unittest.main()
