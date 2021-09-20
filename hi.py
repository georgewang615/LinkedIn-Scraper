from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re as re
import time
import pandas as pd
from collections import Counter

PATH = "C:\\Users\\georg\\Desktop\\chromedriver.exe"
USERNAME = "georgewang615@gmail.com"
PASSWORD = "2572225463Gw"

driver = webdriver.Chrome(PATH)

driver.get("https://www.linkedin.com/uas/login")
time.sleep(3)

email=driver.find_element_by_id("username")
email.send_keys(USERNAME)
password=driver.find_element_by_id("password")
password.send_keys(PASSWORD)
time.sleep(3)
password.send_keys(Keys.RETURN)


list = []
def scrape(link):
    driver.get(link)
    span_title = driver.find_elements_by_class_name("feed-shared-actor__name")
    time.sleep(2)
    for elem in span_title:
        list.append(elem.text)

scrape("https://www.linkedin.com/in/novitacarolina/detail/recent-activity/")

dict = Counter(list)

sorted_dict = sorted(dict.items(), key = lambda x: x[1], reverse = True)

for i in sorted_dict:
    print(i[0], i[1])



driver.close()
