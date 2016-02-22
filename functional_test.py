#!/usr/bin/python3.4
#-*-coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text) # header contains "To-Do"

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item') # input a to-do list

        inputbox.send_keys('Buy paecock feathers') # input "Buy paecock feathers

        inputbox.send_keys(Keys.ENTER) # press enter
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('1: Buy paecock feathers')    # "1: Buy paecock feathers" in To-Do list now

        self.fail('Finish the test!')



if __name__ == '__main__':
    unittest.main()
