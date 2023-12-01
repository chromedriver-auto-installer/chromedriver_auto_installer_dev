from selenium import webdriver
import chromedriver_auto_installer


chromedriver_auto_installer.install()

driver = webdriver.Chrome()
driver.get("http://www.python.org")