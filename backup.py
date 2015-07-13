import json
import os
import requests
import shutil
import sys
import time

USER_ID = os.getenv('INSTAGRAM_USER_ID')
USER_TOKEN = os.getenv('INSTAGRAM_TOKEN')
FEED_URI = 'https://api.instagram.com/v1/users/%s/media/recent/?access_token=%s'
SAVE_DIR = 'backup'


def save_image(image):
    image_id = image['link'].rsplit('/')[4]
    try:
        image_name = image['caption']['text']
    except TypeError:
        image_name = ''

    print 'Fetching [%s] %s' % ( image_id, image_name )

    image_url = image['images']['standard_resolution']['url']
    image_filename = '%s/%s.jpg' % ( SAVE_DIR, image_id )

    # save the JPEG if we don't already have it
    if not os.path.isfile(image_filename):
        response = requests.get(image_url, stream=True)
        with open(image_filename, 'wb') as image_file:
            shutil.copyfileobj(response.raw, image_file)
        del response

    # save the data as JSON
    data_filename = '%s/%s.json' % ( SAVE_DIR, image_id )
    with open(data_filename, 'w') as data_file:
        json.dump(image, data_file, sort_keys=True, indent=4)


max_id = 0
while max_id is not None:
    url = FEED_URI % ( USER_ID, USER_TOKEN )
    if max_id:
        url += '&max_id=%s' % max_id

    data = requests.get(url)
    response = data.json()
    max_id = response['pagination']['next_max_id']
    for image in response['data']:
        save_image(image)
