import numpy as np
from settings import *

def add_appointment(day, time, name, schedule):
	appointment_range = [time, time + dt.timedelta(minutes=20)]

	if not START <= time <= END:
		raise ValueError("Time provided is out of range")
	slot = str(dt.timedelta(days=day, seconds=time.seconds).seconds)
	client_id = get_clientid(name)
	if slot in schedule:
		raise ValueError("Time provided is already occupied")
	else:
		schedule[slot] = client_id
		return schedule

if __name__ == "__main__":
	SCHEDULE = read_csv("schedule.csv")
	SCHEDULE = add_appointment(4, dt.timedelta(hours=8, minutes=40), "Ethan Luh", SCHEDULE)
	SCHEDULE = add_appointment(4, dt.timedelta(hours=9, minutes=40), "Mia Luh", SCHEDULE)
	write_csv("schedule.csv", SCHEDULE)