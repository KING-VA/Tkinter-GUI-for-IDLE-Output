#Importing Modules
import tkinter
import sys
import time

#Setting Up Frame
root = tkinter.Tk()
text_box = tkinter.Text(root, state=tkinter.DISABLED)
text_box.grid(row=0, column=0, columnspan=4)

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
