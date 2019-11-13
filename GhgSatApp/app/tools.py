
"""
.. module:: tools
   :synopsis: Functions that are not directly linked to the web interface and are implementing the core features of the API. 
.. moduleauthor:: Romain Boureau
"""
from datetime import datetime
import os
import pytz
import requests
import math
import shutil
from PIL import Image

API_KEY = 'AIzaSyCMWk5VDZc7t5tuuJQvgU7NKpJ6OqjyWZI'
zoom = 13
API_URL = ('https://maps.googleapis.com/maps/api/staticmap?center={},{}&zoom={}&size=514x257&key={}&maptype=satellite')
def query_api(latitude,longitude,path):
     """

        **Google Maps API query**
        
        This function is used to query a satellite image using the latitude and longitude parameters and save it to the relative path given as parameter.
     
        :param latitude: latitude used for the Google Maps API query
        :type latitude: int

        :param longitude: longitude used for the Google Maps API query
        :type longitude: int

        :param path: the path to where the file will be saved
        :type path: String

        :return: void
    """
     try:
          print(API_URL.format(latitude,longitude,zoom, API_KEY))
          data = requests.get(API_URL.format(latitude,longitude,zoom, API_KEY), stream=True)
          if data.status_code == 200:
              with open(path, 'wb') as f:
                  data.raw.decode_content = True
                  shutil.copyfileobj(data.raw, f)    
     except Exception as exc:
          print(exc)
          data = None
def fusionImages(pathBackground,pathOverlay,pathFusioned):
     """

        **Image Fusion**
        
        This function is used to overlay the image situated at pathOverlay on the pathBackground image. The result is saved at pathFusioned.
     
        :param pathBackground: path to the image being overlaid
        :type pathBackground: String

        :param pathOverlay: path to the overlaying image 
        :type pathOverlay: String
        
        :param pathFusioned: path to the result image
        :type pathFusioned: String

        :return: the result image stored at pathFusioned
    """
     til = Image.new("RGB",(514,257))
     background = Image.open(pathBackground)
     overlay = Image.open(pathOverlay)
     til.paste(background)
     til.paste(overlay, mask=overlay)

          
     til.save(pathFusioned,"PNG")

     return til

     
