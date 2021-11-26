
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/testworks/Desktop/chromedriver_win32_11.19/chromedriver.exe")

driver.get("https://www.naver.com")
driver.close()