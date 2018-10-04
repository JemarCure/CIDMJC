from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

                       
class NewVisitorTest(unittest.TestCase):
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
table = self.browser.find_element_by_id('id_list_table')
def setUp(self):
        self.browser = webdriver.Firefox()
def tearDown(self):
        self.browser.quit()
 # When she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list table
inputbox.send_keys(Keys.ENTER)
time.sleep(1)
self.check_for_row_in_list_table('1: Buy peacock feathers')

    # There is still a text box inviting her to add another item. She
    # enters "Use peacock feathers to make a fly" (Edith is very
    # methodical)
inputbox = self.browser.find_element_by_id('id_new_item')
inputbox.send_keys('Use peacock feathers to make a fly')
inputbox.send_keys(Keys.ENTER)
time.sleep(1)

    # The page updates again, and now shows both items on her list
self.check_for_row_in_list_table('1: Buy peacock feathers')
self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

    # Edith wonders whether the site will remember her list. Then she sees
[...]

def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


def test_can_start_a_list_and_retrieve_it_later(self):
        [...]