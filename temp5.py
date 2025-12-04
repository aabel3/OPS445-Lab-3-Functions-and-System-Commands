#!/usr/bin/env python3
# OPS445 - Lab 3
# temp5.py
# Author: Avraham Abel

def describe_temperature(temp):
	if temp > 30:
		return 'hot'
	elif temp < 0:
		return 'cold'
	elif temp == 20:
		return 'perfect'
	else:
		print("And also, .....")
	return 'ok'

print(describe_temperature(20))	
