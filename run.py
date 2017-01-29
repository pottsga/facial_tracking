"""
  * A script that first poses the Preferences pane to a user to gather some data-entry
  * information, then multi-threads two scripts to run concurrently.
"""
import threading
from threading import Thread
import os

def runDetect():
	os.system("python3 facial_detection.py") #run the facial detection portion
def runGUI():
	os.system("python3 gui.py") #run the gui portion
def startThreading():
	Thread(target = runDetect).start()
	Thread(target = runGUI).start()
def getUserInput():
	os.system("python3 form.py") #run the user-input script (Preferences pane)
def exit_all():
	exit()

#--------------------------------------------------------------
getUserInput() #since we don't want the form to run at the same time as the rest of the threaded scripts
startThreading() #start multi-threading
	
