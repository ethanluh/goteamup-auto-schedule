import importlib  
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import date, datetime, timedelta

wbscrape = importlib.import_module("webbrowser-scraper")
encd = importlib.import_module("encode")

driver = wbscrape.driver

def click(search_type, value):
	button = WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((search_type, value)))
	# actions = ActionChains(driver)
	# actions.move_to_element(button)
	# actions.click(button)
	# actions.perform()
	# elem = driver.find_element(search_type, value)
	print(button)
	driver.execute_script('arguments[0].click();',[button])

def create_appointment(scrape_data, appointment_dati):
	link = "https://goteamup.com/providers/appointments/" + scrape_data[0] + "/book?instructor=" + scrape_data[2] + "&customer_id=" + scrape_data[1] + "&encoded_appointment_slot_data=" + encd.generate_appointment_code(appointment_dati)
	driver.get(link)
	click(By.XPATH, "//button[contains(text(),'Book')]")
	return scrape_data, appointment_dati
	# click(By.CSS_SELECTOR, 'button.btn.btn-primary.btn-block')

def schedule_weekly(scrape_data, appointment_datis, amount):
	weekday_offsets = []
	for i in range(len(appointment_datis)):
		offset = appointment_datis[i].day - date.today().weekday()
		weekday_offsets.append(offset if offset > 0 else offset + 7)
	weekday_offsets.sort()
	for i in range(amount):
		print(create_appointment(scrape_data, appointment_datis[7*np.floor(i/len(appointment_datis))+weekday_offsets[i%len(appointment_datis)]]))

def book_package(customer, appointment_type, pack_size, appointment_times, primary_coach):
	scrape_data = wbscrape.scrape_page(customer, primary_coach)
	schedule_weekly(scrape_data, appointment_times, pack_size)

# book_package("Amy Smith", "Private Lesson", 40, [[0, 19, 20], [0, 19, 40], [2, 20, 00], [4, 19, 40]], "Armin Arlelt")
create_appointment(['140744', '5977322', '118289'], datetime(2022, 9, 19, 19, 20))



