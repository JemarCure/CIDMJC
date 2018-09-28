from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

class NewVisitorTest(unittest.TestCase):
  
     def setUp(self):
        self.browser = webdriver.Firefox()
  
        self.assertTrue(
        any(row.text == '1: Buy peacock feathers' for row in rows),
        "New to-do item did not appear in table"
    )
