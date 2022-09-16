import importlib  
import numpy as np
from datetime import date, datetime, timedelta

wbscrape = importlib.import_module("webbrowser-scraper")
driver = wbscrape.driver

def click(search_type, value):
	button = wait.until(expected_conditions.element_to_be_clickable((search_type, value)))
	actions = ActionChains(driver)
	actions.move_to_element(button)
	actions.click(button)
	actions.perform()

def create_appointment(scrape_data, appointment_info):
	link = "https://goteamup.com/providers/appointments/" + scrape_data[0] + "/book?instructor=" + scrape_data[2] + "&customer_id=" + scrape_data[1] + "&encoded_appointment_slot_data=" + generate_appointment_code(appointment_info)
	# print(appointment_info[0])
	driver.get(link)
	click(By.CSS_SELECTOR, 'button.btn.btn-primary.btn-block')

def schedule_weekly(scrape_data, appointment_times, amount):
	offsets = []
	for i in range(len(appointment_times)):
		offset = appointment_times[i][0] - date.today().weekday()
		offsets.append(offset if offset > 0 else offset + 7)
	offsets.sort()
	for i in range(amount):
		create_appointment(scrape_data, [date.today() + timedelta(7*np.floor(i/4)+offset[i%4]), appointment_times[i%4][1], appointment_times[i%4][2]])

def book_package(customer, appointment_type, pack_size, appointment_times, primary_coach):
	scrape_data = wbscrape.scrape_page(customer, primary_coach)
	schedule_weekly(scrape_data, appointment_times, pack_size)

book_package("Amy Smith", "Private Lesson", 40, [[0, 19, 20], [0, 19, 40], [2, 20, 00], [4, 19, 40]], "Armin Arlelt")