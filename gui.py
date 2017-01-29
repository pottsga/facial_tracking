"""
   * A script that makes the gui pane, and also reads a file (coord_file) that contains
   * some data being written by facial_detection.py. This data is where to put the cursor
   * given the data given by the facial detection.
"""
from tkinter import *

root = Tk()

pref_wid = 640 #the same dims as the facial_detection pane
pref_height = 400

w = Canvas(root, width=pref_wid, height=pref_height)

global rect

rect = 0 #'delete' the rect

def update():
	global rect

	coord_file = open("data_files/coords.txt", "r")
	coords = str(coord_file.read()).split(",")
	coord_file.close()

	rect_tup = (0,0,0+20, 0+20)

	if coords != ['']: # if the coords list is not null
		rect_tup = (int(coords[0]), int(coords[1]), int(coords[0])+20, int(coords[1])+20)

	if rect is not 0: # if we didn't already set the old rect to 0, delete it (we don't want a trailing group of rectangles)
		w.delete(rect)

	rect = w.create_rectangle(rect_tup, fill='', outline='blue', width=2)
	
	root.after(100, update)


update()
w.pack()
root.mainloop()
