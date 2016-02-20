#!/usr/bin/python3.4
#-*-coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text) # header contains "To-Do"

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item') # input a to-do list

        inputbox.send_keys('Buy paecock feathers') # input "Buy paecock feathers

        inputbox.send_keys(keys.Enter) # press enter

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy paecock feathers' for row in rows)
        )    # "1: Buy paecock feathers" in To-Do list now

        self.fail('Finish the test!')



if __name__ == '__main__':
    unittest.main()
