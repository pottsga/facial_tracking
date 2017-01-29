"""
   * This script is the portion of the project that does the facial detection. It takes in
   * the haarcascades/(whichever cascade it needs).xml file it needs and uses that to detect.
   * It writes out to the data_files/coords.txt file which is used by the gui script
   * to draw the cursor.
"""
import cv2
from tkinter import *
from timeit import default_timer as timer

start = timer() #start the timer

wears_glasses = True

userinfo_file = open("data_files/userinfo.txt", "r")
userinfo = userinfo_file.read().split(",")

int_glasses = int(userinfo[0])
name = userinfo[1]
override_glasses_correction = int(userinfo[2])
lighting_conds_int = int(userinfo[3])
override = False

lighting_conds = "Optimal"

if lighting_conds_int == 2:
	lighting_conds = "Sub-optimal"

haarcascade = ""

if override_glasses_correction is not 1:
	if int_glasses == 2:
		wears_glasses = False
		haarcascade = "haarcascades/haarcascade_frontalface_alt.xml"
	elif int_glasses == 1:
		wears_glasses = True
		haarcascade = "haarcascades/haarcascade_frontalface_default.xml"
else:
	override = True
	haarcascade = "haarcascades/haarcascade_frontalface_default.xml" # because it was overridden for testing purposes

face_cascade = cv2.CascadeClassifier(haarcascade)

cap = cv2.VideoCapture(0)

total_faces_found = 0 # used for data collection
total_iterations = 0

while True:
	
	ret, img = cap.read()
	gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x, y, w, h) in faces:

		total_faces_found += 1 # iterate the total faces found
		coord_file = open("data_files/coords.txt", 'w')
		box = str(x)+","+str(y)
		coord_file.write(box)
		coord_file.close()
		
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
	
	total_iterations += 1 #iterate the toal iterations
	cv2.imshow('Press ESC to Exit -- Facial Detection', img)

	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

end = timer() # end the timer
total_time = end - start                                       
text = name+","+str(total_faces_found)+","+str(total_iterations)+","+str(total_faces_found/total_iterations)+","+str(total_iterations-total_faces_found)+","+str(wears_glasses)+","+str(override)+","+str(lighting_conds)+","+str(total_iterations/total_time)+"\n"
with open("data_files/data_log.csv", "a") as logfile:
    logfile.write(text)


cap.release()
cv2.destroyAllWindows()



