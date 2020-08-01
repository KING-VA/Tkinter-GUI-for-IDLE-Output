#Importing Modules
import tkinter
import sys
import time

#Setting Up Frame
root = tkinter.Tk()
root.grid_propagate(False)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
text_box = tkinter.Text(root, state=tkinter.DISABLED)
text_box.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
scrollb = ttk.Scrollbar(root, command=text_box.yview)
scrollb.grid(row=0, column=1, sticky='nsew')
text_box['yscrollcommand'] = scrollb.set

#Creating Functions
def write(string):
    text_box.config(state=tkinter.NORMAL)
    text_box.insert("end", string + "\n")
    text_box.see("end")
    text_box.config(state=tkinter.DISABLED)
    root.update()
def looptime_write(sec, times, string):
    write("Printing "+string+" every "+str(sec)+" seconds for "+str(times)+" times.")
    for _ in range(times): 
        write(string)
        time.sleep(sec)

#Main Code
write("Hello World")
looptime_write(5, 2, "Hello World")
looptime_write(10, 3, "Hello World")
looptime_write(2, 5, "Hello World")
looptime_write(3, 10, "Hello World")
write("Completed")
