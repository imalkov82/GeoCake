#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2013 gily <gily@gily-HP-G62-Notebook-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import threading
import time

g_events_array = []

def gDeclare_events(numOfEvents):
	events = []
	for i in range(0, numOfEvents):
		events.append(threading.Event())
	for event in events:
		event.clear()
	return events
	
class interpolator(threading.Thread):
	localEventNum = 0
	def run(self):
		for i in range(0, 5):
			print('interpolator alive')
			time.sleep(1)
		print('interpolator done.')
	
	def interSetEvent(self):
		interEvent.set()
		
class dbHandler(threading.Thread):
	localEventNum = 1
	def run(self):
		for i in range(0, 5):
			print('debHandler alive')
			time.sleep(0.5)
		print('dbHandelr done.')

def main():
	global g_events_array
	#Create events and set to global array
	g_events_array = gDeclare_events(2)
	
	#Create threads
	inter = interpolator()
	dbh = dbHandler()
	
	print('Starting threads')
	inter.start()
	dbh.start()
	
	#Sleep on events
	
	
	print('Joinning inter')
	inter.join()
	print('main: dbh.isAlive', dbh.isAlive())
	print('joining dbh')
	dbh.join()
	
	# Receive the events from other threads
	print('Exiting')
	return 0

if __name__ == '__main__':
	main()

