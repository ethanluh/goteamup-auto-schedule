import numpy as np
from settings import *
from schedule import *

#pushes appointments to teamup server
#takes first day of month, month number, and appointment
def push_appointment():
	print()

if __name__ == "__main__":
	SCHEDULE = read_csv("schedule.csv")
	SCHEDULE = schedule_appointment(4, dt.timedelta(hours=10, minutes=40), "Ethan Luh", SCHEDULE)
	# SCHEDULE = add_appointment(4, dt.timedelta(hours=9, minutes=40), "Mia Luh", SCHEDULE)
	write_csv("schedule.csv", SCHEDULE)