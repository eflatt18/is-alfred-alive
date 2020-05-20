import sys
import os
from twython import Twython
from picamera import PiCamera
from time import sleep


CONSUMER_KEY = 'consumer key here'
CONSUMER_SECRET = 'consumer secret here'
ACCESS_KEY = 'access key here'
ACCESS_SECRET = 'access secret here'

#other cameras will require different code
camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('/home/pi/image.jpg')
camera.stop_preview()

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
photo = open('image.jpg','rb')
image_ids = api.upload_media(media=photo)
api.update_status(status='', media_ids=image_ids['media_id'])
