import numpy as np
from datetime import date, datetime, timedelta
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

##-- TESTING --##
customer = {
  "Amy Smith": 5977322,
  "James Smith": 5977320,
  "John Smith": 5977337
}
classes = {
  "Private Lesson": 140744,
}
instructor = {
  "Armin Arlelt": 118289,
  "Ethan Luh": 118191
}

appointments = [
	["Private Lesson", "Armin Arlelt", "Amy Smith", [[0, 7, 20], [0, 7, 40], [2, 7, 20], [4, 7, 20]], 40],
	["Private Lesson", "Ethan Luh", "James Smith", [[0, 7, 20], [0, 7, 40], [2, 7, 20], [4, 7, 20]], 20]
]

master_login = ["ethanluh@gmail.com", "15kangarooKS@"]

##-- BEGIN --##

def initialize(login, headless, true):
	initialize_webdriver(headless)
	initialize_goteamup(master_login, test)

def close():
	driver.quit()

def wait(sec):
	wait = WebDriverWait(driver, sec)
	return wait

def initialize_webdriver(headless=False):
	global options 
	global driver
	options = webdriver.ChromeOptions()
	# print(headless)
	if headless:
		options.add_argument('headless')
	driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

def initialize_goteamup(login, test = True):
	driver.get("https://goteamup.com/providers/reporting/dashboard/")
	driver.find_element("name", "email-email").send_keys(login[0] + Keys.RETURN)
	driver.find_element("name", "login-password").send_keys(login[1] + Keys.RETURN)
	if test:
		driver.find_element("id", "headlessui-menu-button-1").click()
		driver.find_element("id", "headlessui-menu-item-4").click()

def click(search_type, value):
	button = wait.until(expected_conditions.element_to_be_clickable((search_type, value)))
	actions = ActionChains(driver)
	actions.move_to_element(button)
	actions.click(button)
	actions.perform()

def create_appointment(class_type, coach, student, appointment_info):
	link = "https://goteamup.com/providers/appointments/" + str(classes[class_type]) + "/book?instructor=" + str(instructor[coach]) + "&customer_id=" + str(customer[student]) + "&encoded_appointment_slot_data=" + generate_appointment_code(appointment_info)
	print(appointment_info[0])
	driver.get(link)
	click(By.CSS_SELECTOR, 'button.btn.btn-primary.btn-block')

def schedule_weekly(scheduling_info):
	offsets = []
	for i in range(len(days)):
		offset = days[i][0] - date.today().weekday()
		offsets.append(offset if offset > 0 else offset + 7)
	offsets.sort()
	for i in range(amount):
		print(i)
		# create_appointment("Private Lesson", "TEST STAFF", "TEST TEST", [date.today() + timedelta(days=7*np.floor(i/len(days)) + offsets[i%len(days)]), days[i%len(days)][1], days[i%len(days)][2]])

# def schedule_all()
initialize(master_login, True, True)
schedule_weekly(classes["Private Lesson"], instructor["Armin Arlelt"], customer["Amy Smith"], [[0, 7, 20], [0, 7, 40], [2, 7, 20], [4, 7, 20]], 40)
wait(20)
close()