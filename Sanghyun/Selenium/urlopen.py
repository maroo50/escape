from selenium import webdriver

driver = webdriver.Chrome("C:\pydata\chromedriver_win32\chromedriver.exe")

driver.get("https://www.naver.com/")
driver.close