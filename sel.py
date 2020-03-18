# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:51:07 2020

@author: ritesh
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
driver = webdriver.Chrome()
driver.get('https://google.com')
elem = driver.find_element(By.XPATH,'//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
elem.clear()
elem.send_keys("Gulzar")
elem.send_keys(Keys.RETURN)

