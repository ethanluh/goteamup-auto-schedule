import unittest
import datetime as dt
import schedule

#tests if add_appointment accepts times that are outside of given range
def time_range():
	if schedule.add_appointment(4, dt.timedelta(hours=6, minutes=40), "Ethan") == 1:
		return("clear")
	else:
		return("add_appointment accepting times out of range")
		
if __name__ == "__main__":
	SCHEDULE = {}
	print(time_range())
	print("Tests Complete")
