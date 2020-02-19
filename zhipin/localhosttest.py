# -*- coding: utf-8 -*-
# from selenium import selenium
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# import time
# from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1920,1080))
display.start()
driver = webdriver.Firefox()
driver.get("http://www.python.org")
# driver.get("https://www.zhipin.com/job_detail/?query=python&scity=101010100&industry=&position=")
print(driver.page_source)
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()
display.stop()