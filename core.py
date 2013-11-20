#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  core.py
#  
#  Copyright 2013 gily <gilymerkado@gmail.com, igor.malkov82@gmail.com>
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
import logging

logging.basicConfig(level=logging.DEBUG, 
	format='[%(levelname)s] (%(threadName)-12s) %(message)s',
	)
	
class interpolator(threading.Thread):
	def __init__(self, group=None, target=None, name=None,
		args=(), kwargs=None, verbose=None):
			threading.Thread.__init__(self, group=group, target=target,
				name=name, verbose=verbose)
			self.event = args[0]
			return
        
	def run(self):
		logging.debug('running')
		time.sleep(5)
		logging.debug('setting event')
		self.setEvent(self.event)
		logging.debug('Done')
	
	def setEvent(self, event):
		event.set()
		
class dbHandler(threading.Thread):
	def __init__(self, group=None, target=None, name=None,
		args=(), kwargs=None, verbose=None):
			threading.Thread.__init__(self, group=group, target=target,
				name=name, verbose=verbose)
			self.event = args[0]
			return
        
	def run(self):
		logging.debug('running')
		time.sleep(0.5)
		logging.debug('setting event')
		self.setEvent(self.event)
		logging.debug('Done')
	
	def setEvent(self, event):
		event.set()

def main():
	#Create an event
	event = threading.Event()
	
	#Create threads
	inter = interpolator(name='interpolator', args=(event,))
	dbh = dbHandler(name='dbHandler', args=(event,))
	
	threads = [inter, dbh]
	
	logging.debug('Starting threads')
	inter.start()
	dbh.start()
	
	#Sleep on events
	logging.debug('sleeping on event')
	event.wait()
	while True:
		#check which thread is still working
		if event.isSet():
			logging.debug('saw event.isSet(). Checking who set it')
			if inter.isAlive():
				logging.debug('interpolator is still alive')
				if dbh.isAlive():
					logging.debug('dbHandler is still alive. Unknown set the event')
				else:
					logging.debug('dbHandler is not alive. dbh set the event. keep waiting for interpolator')
					logging.debug('clear the event')
					event.clear()
			else:
				logging.debug('interpolator is not alive')
				if dbh.isAlive():
					logging.debug('dbHandler not alive. interpolator set the event.Wait for dbHandler')
					logging.debug('clear the event')
					event.clear()
				else:
					logging.debug('Both threads not alive. can continue')
					break
	
	# Receive the events from other threads
	logging.debug('Exiting')
	return 0

if __name__ == '__main__':
	main()

