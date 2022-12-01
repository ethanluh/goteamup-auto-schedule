import importlib  
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import date, datetime, timedelta


encd = importlib.import_module("encode")
print(encd.generate_appointment_code(datetime(2022, 12, 20, 19, 20)))
wbscrape = importlib.import_module("webbrowser-scraper")


driver = wbscrape.driver

def click(search_type, value):
	# driver.manage().timeouts().setScriptTimeout(20, TimeUnit.SECONDS);	
	# driver.executeAsyncScript("window.setTimeout(arguments[arguments.length - 1], 5000);");	
	# WebElement button =driver.findElement(By.name("btnLogin"));
	button = WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((search_type, value)))
	driver.execute_script('arguments[0].click();',button)

def create_appointment(scrape_data, appointment_dati):
	link = "https://goteamup.com/providers/appointments/" + scrape_data[0] + "/book?instructor=" + scrape_data[2] + "&customer_id=" + scrape_data[1] + "&encoded_appointment_slot_data=" + encd.generate_appointment_code(appointment_dati)
	# link = "https://goteamup.com/providers/appointments/140744/book?instructor=111114&customer_id=5977322&encoded_appointment_slot_data=eyJpbnN0cnVjdG9yIjogMTExMTE0LCAidmVudWUiOiA0NDEwMiwgInZlbnVlX3Jvb20iOiBudWxsLCAib2ZmZXJpbmdfdHlwZSI6IDE0MDc0NCwgInN0YXJ0X3RpbWUiOiAiMjAyMi0xMi0yMFQxOToyMDowMCIsICJlbmRfdGltZSI6ICIyMDIyLTEyLTIwVDE5OjQwOjAwIn0="
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

book_package("Amy Smith", "Private Lesson", 5, [[0, 19, 20], [0, 19, 40], [2, 20, 00], [4, 19, 40]], "Armin Arlelt")
# create_appointment(['140744', '5977322', '111114'], datetime(2022, 12, 20, 19, 20))
# print(encd.generate_appointment_code(datetime(2022, 12, 20, 19, 20)))



