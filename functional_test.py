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
 # There is still a text box inviting her to add another item. She
    # enters "Use peacock feathers to make a fly" (Edith is very
    # methodical)
inputbox = self.browser.find_element_by_id('id_new_item')
inputbox.send_keys('Use peacock feathers to make a fly')
inputbox.send_keys(Keys.ENTER)
time.sleep(1)

    # The page updates again, and now shows both items on her list
table = self.browser.find_element_by_id('id_list_table')
rows = table.find_elements_by_tag_name('tr')
self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
self.assertIn(
        '2: Use peacock feathers to make a fly',
         [row.text for row in rows]
    )

    # Edith wonders whether the site will remember her list. Then she sees
    # that the site has generated a unique URL for her -- there is some
    # explanatory text to that effect.
self.fail('Finish the test!')

    # She visits that URL - her to-do list is still there.