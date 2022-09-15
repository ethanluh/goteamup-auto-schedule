import importlib  
from selenium.webdriver.common.by import By
goinit = importlib.import_module("goteamup-initialize")

driver = goinit.initialize()

def scrape_page(customer, coach):
	scrape_data = [
		"140744",
		get_customer_id(customer),
		get_coach_id(coach)
	]
	return scrape_data

def get_customer_id(name):
	data_source = "https://goteamup.com/providers/customers/?status=0&status_tag=0"
	driver.get(data_source)
	customer_id = driver.find_element(By.XPATH, "//a[contains(text(),'" + name + "')]").get_attribute('href')
	return customer_id[-8:-1]

def get_coach_id(name):
	data_source = "https://goteamup.com/providers/configure/staff/"
	driver.get(data_source)
	coach_id = driver.find_element(By.XPATH, "//h4[contains(text(),'" + name + "')]//ancestor::div[4]//a[contains(text(),'/providers/configure/staff/')]").get_attribute('href')
	return coach_id

print(get_coach_id("Armin Arlelt"))

