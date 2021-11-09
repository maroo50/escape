from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\pydata\chromedriver_win32\chromedriver.exe')



driver.get("http://www.naver.com/")
driver.close
elem = driver.find_element_by_name("query")
elem.send_keys("python")
elem.send_keys(Keys.RETURN)
