import sys
import os
from twython import Twython
from picamera import PiCamera
from time import sleep

# go here and create a new app: https://apps.twitter.com
# then click "key and access tokens" to generate them
# put them inside the quotes below

CONSUMER_KEY = 'consumer key here'
CONSUMER_SECRET = 'consumer secret here'
ACCESS_KEY = 'access key here'
ACCESS_SECRET = 'access secret here'


# this runs the following script from the command line that takes the photo and saves it
# it will only work for USB webcams,
# you'll have to do something different if you're using a pi-cam
camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('/home/pi/image.jpg')
camera.stop_preview()

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
photo = open('image.jpg','rb')
image_ids = api.upload_media(media=photo)
api.update_status(status='', media_ids=image_ids['media_id'])