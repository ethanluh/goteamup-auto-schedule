import string
import numpy as np
from datetime import date, datetime, timedelta

ALPH_CODE = np.concatenate((list(string.ascii_uppercase), list(string.ascii_lowercase), ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]))

def baseN(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
	return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def simple_encode(n):
	d1 = int(n[slice(1)])
	d2 = int(n[slice(1,2)])
	return ALPH_CODE[4*d1] + ALPH_CODE[d2+48]

def complex_encode(n, zero, offset):
	d1 = int(n[slice(1)])
	d2 = int(n[slice(1,2)])
	based_d2 = ("0" + baseN(d2, 4))[-2:]
	return zero + ALPH_CODE[d1 + 48] + ALPH_CODE[int(based_d2[slice(1)]) + 12] + ALPH_CODE[(int(based_d2[slice(1,2)]) * 16 + offset)%62]

def generate_appointment_code(appointment_info):
	appointment_date, hour, minute = appointment_info
	year_string = str(appointment_date.year)[slice(2, 4)]
	month_string = ("0" + str(appointment_date.month))[-2:]
	day_string = ("0" + str(appointment_date.day))[-2:]
	s_hour_string = ("0" + str(hour))[-2:]
	s_min_string = ("0" + str(minute))[-2:]
	e_hour_string = ("0" + str(hour + int(np.floor((minute+20)/60))))[-2:]
	e_min_string = ("0" + str((minute+20)%60))[-2:]
	base = 'eyJpbnN0cnVjdG9yIjogMTExMDUyLCAidmVudWUiOiA0NDEwMiwgInZlbnVlX3Jvb20iOiBudWxsLCAib2ZmZXJpbmdfdHlwZSI6IDE0MDc0NCwgInN0YXJ0X3RpbWUiOiAiMj'
	appointment_code = base + complex_encode(year_string, "A", 2)
	appointment_code += complex_encode(month_string, "0", 2) 
	appointment_code += complex_encode(day_string, "0", 5) 
	appointment_code += complex_encode(s_hour_string, "Q", 3)
	appointment_code += complex_encode(s_min_string, "o", 3)
	appointment_code += complex_encode("00", "o", 2)
	appointment_code += "IsICJlbmRfdGltZSI6ICIyMD"
	appointment_code += simple_encode(year_string)
	appointment_code += "LT" + simple_encode(month_string)
	appointment_code += "LT" + simple_encode(day_string)
	appointment_code += "VD" + simple_encode(e_hour_string)
	appointment_code += "Oj" + simple_encode(e_min_string)
	appointment_code += "Oj" + simple_encode("00") + "In0="

	return appointment_code