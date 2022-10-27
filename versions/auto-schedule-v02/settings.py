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

def write_csv(file, d):
	w = csv.writer(open(file, "w"))
	for key, val in d.items():
		w.writerow([key, val])

def read_csv(file):
	try:
		csv_file = open(file, "r")
	except:
		csv_file = open(file, "w")
	r = csv.reader(csv_file)
	d = {}
	for row in r:
		d[row[0]] = row[1]
	return d

CLIENTS = read_csv("clients.csv")

def get_clientid(name):
	name = name.lower()
	if not name in CLIENTS:
		try:
			CLIENTS[name] = str(int(list(CLIENTS.items())[-1][1]) + 1)
		except:
			CLIENTS[name] = 100
	write_csv("clients.csv", CLIENTS)
	return str(CLIENTS[name])