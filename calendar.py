#!/usr/bin/python
#coding:utf-8

import sys
import datetime 

week_day = ["日", "月", "火", "水", "木", "金", "土"]
month = [31,28,31,30,31,30,31,31,30,31,30,31]

def print_calendar(y, m):
	day = 365 * (y-1) + y / 4 - y / 100 + y / 400 + sum(month[0 : m - 1]) + 1
	first = day % 7

	print "    %d月　%d年" % (m, y)
	for w in week_day: print w ,
	print
	for space in range(first): print "  ",
	for cal in range(1, month[m - 1] + 1): 
		if first % 7 == 0: 
			print
		print "%2d" % (cal),
		first += 1

if __name__ == "__main__":
	argc = len(sys.argv)
	if argc == 1:
	  	d = datetime.datetime.today()
		print_calendar(d.year, d.month)
		
	elif argc == 2:
		date = sys.argv[1].split("-")
		date = [int(x) for x in date]
		y, m, d = date[0], date[1], date[2] 

		day = 365 * (y-1) + y / 4 - y / 100 + y / 400 + sum(month[0 : m - 1]) + d
		print week_day[day % 7] + "曜日"

	elif argc == 3:
		date = []
		day = []
		for i in range(2):
			date.append(sys.argv[i + 1].split("-"))
			date[i] = [int(x) for x in date[i]]

		for i in range(2):
			y, m, d = date[i][0], date[i][1], date[i][2]
			day.append(365 * (y-1) + y / 4 - y / 100 + y / 400 + sum(month[0 : m - 1]) + d)
		print abs(day[1] - day[0])
	
	 
	  
	   
