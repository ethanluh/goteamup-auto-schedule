import numpy as np
from settings import *


# SCHEDULE = np.zeros((7, NUM_SLOTS),dtype=int)

def add_appointment(day, time, name):
	appointment_range = [time, time + dt.timedelta(minutes=20)]

	if (END - appointment_range[0]).days < 0 or (appointment_range[0] - START).days < 0:
		return print("Time is out of range")
	slot = str(dt.timedelta(days=day, seconds=time.seconds))
	client_id = get_clientid(name)
	if slot in SCHEDULE:
		return print("There is already an appointment scheduled for that time")
	else:
		SCHEDULE[slot] = client_id
		write_csv("schedule.csv", SCHEDULE)
		return print(str(client_id) + " successfully scheduled an appointment for " + WEEK[day] + " at " + str(time))


if __name__ == "__main__":
	SCHEDULE = read_csv("schedule.csv")
	add_appointment(4, dt.timedelta(hours=7, minutes=40), "Ethan")