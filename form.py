"""
   * A script that asks the user for some data that will be used later on in the data
   * gathering/analysis portion of my project. Called before the other two scipts
   * are multi-threaded
"""
from tkinter import *

root = Tk()
root.wm_title("Preferences")

username_label = Label(root, text="Name ")
username_label.pack(side = TOP)

username_entry = Entry(root, bd = 5)
username_entry.pack(side=TOP)

v = IntVar()
v.set(1) # initialize to yes

glasses_label = Label( root, text="Do you wear glasses?").pack()
Radiobutton(root, text="Yes", padx = 20, variable=v, value=1).pack(anchor=W)
Radiobutton(root, text="No", padx = 20, variable=v, value=2).pack(anchor=W)

override = IntVar()
c = Checkbutton(root, text="Override glasses correction?", variable = override).pack(side=TOP)

lighting_conds = IntVar()
lighting_conds.set(1)

lighting_label = Label(root, text="Lighting conditions?").pack()
Radiobutton(root, text="Optimal", padx=20, variable = lighting_conds, value=1).pack(anchor=W)
Radiobutton(root, text="Sub-optimal", padx=20, variable=lighting_conds, value=2).pack(anchor=W)


def submit():
	
	userinfo_file = open("data_files/userinfo.txt", "w")
	userinfo_file.write(str(v.get())+","+username_entry.get()+","+str(override.get())+","+str(lighting_conds.get()))
	userinfo_file.close()

	exit()

submit = Button(root, text ="Submit", command = submit)
submit.pack(side =BOTTOM) 

root.mainloop()
