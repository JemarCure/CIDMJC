from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium import webdriver

from django.test import LiveServerTestCase
from selenium import webdriver


browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title
class NewVisitorTest(LiveServerTestCase):
          
        def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
                 self.browser.get(self.live_server_url)     
                        def setUp(self):