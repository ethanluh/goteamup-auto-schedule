import datetime as dt
import csv

START = dt.timedelta(hours=7) #slots start at 7am
END = dt.timedelta(hours=21) #slots end at 9pm
INTERVAL = dt.timedelta(minutes=20) #slot every 20 minutes
NUM_SLOTS = int((END - START)/INTERVAL) #slots per day
TODAY = dt.datetime.today().weekday()
WEEK = {
	0: "Monday",
	1: "Tuesday",
	2: "Wednesday",
	3: "Thursday",
	4: "Friday",
	5: "Saturday",
	6: "Sunday",
}
def read_csv(filename, fields):
	file = open(filename, 'a')
	row_count = file.line_num
	print(row_count)
	csv.DictReader(file, fieldnames=fields)