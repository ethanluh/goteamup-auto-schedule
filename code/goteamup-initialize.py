from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

master_login = ["ethanluh@gmail.com", "15kangarooKS@"]

def initialize_webdriver(headless):
	global driver
	options = webdriver.ChromeOptions()
	if headless:
		options.add_argument('headless')
	driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
	return driver

def initialize_goteamup(login, test):
	driver.get("https://goteamup.com/login")
	driver.find_element("name", "email-email").send_keys(login[0] + Keys.RETURN)
	driver.find_element("name", "login-password").send_keys(login[1] + Keys.RETURN)
	if test:
		driver.find_element("id", "headlessui-menu-button-1").click()
		driver.find_element("id", "headlessui-menu-item-4").click()

def initialize(headless = False, test = True, login = master_login):
	driver = initialize_webdriver(headless)
	initialize_goteamup(login, test)
	return driver

def close():
	driver.quit()