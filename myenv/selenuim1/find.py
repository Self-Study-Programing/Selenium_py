from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

query_txt = input('크롤링할 키워드는 무엇입니까')

# path = "/Users/seonghun/Downloads/chromedriver"
driver = webdriver.Chrome()

driver.get('https://korean.visitkorea.or.kr/main/main.html')
time.sleep(2)

# driver.find_element(By.ID, 'btnSearch').click()

element = driver.find_element(By.ID,'inp_search')

element.send_keys(query_txt)

driver.find_element(By.LINK_TEXT,'검색').click()

time.sleep(5)