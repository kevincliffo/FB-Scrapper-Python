import requests
import os

from dotenv import load_dotenv

load_dotenv()

class FBScrapper(object):
    def __init__(self):
        self._access_token = os.environ.get('ACCESS_TOKEN')
        self.page_id = os.environ.get('PAGE_ID')

    def get_page_posts(self):
        url = f'https://graph.facebook.com/{self.page_id}/posts?access_token={self._access_token}'
        response = requests.get(url)

        data = response.json()

        for post in data['data']:
            print('message : ' + str(post))

    def get_page_post_comments(self, post_id):
        url = f'https://graph.facebook.com/{post_id}/comments?access_token={self._access_token}'
        response = requests.get(url)
        
        data = response.json()