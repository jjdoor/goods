# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class test002(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://gaoqing.la/3d")
        self.selenium.start()
    
    def test_test002(self):
        sel = self.selenium
        sel.open("/3d")
        sel.click(u"link=下一页")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
