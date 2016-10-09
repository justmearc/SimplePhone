import Tkinter
from Tkinter import tkMessageBox
import serial, time

master = Tkinter.Tk()

class SerialPort():
    def __init__(self):
       self.baud_rate = 115200

    def connect(self):
        #open connection
        self.serialport = serial.Serial("/dev/ttyAMA0", self.baud_rate, timeout=0.5)
    def transmit(self, data):
        self.serialport.write(data + '\r')
class Phone():
    def _init_(self,fona):
        self.fona = serialport.SerialPort()
        self.fona.transmit('AT+CHFA=0')
    def MakeCall(self):
        self.fona.transmit('ATD' + ('17153098886' ;')
        tkMessageBox.showinfo("Calling")
    def EndCall(self):
        self.fona.transmit('ATH')

A = Tkinter.Button(master, text="Call", command = self.MakeCall())
A.grid(column=0, row=1)
B = Tkinter.Button(master, text="End", command = self.EndCall())
B.grid(column=1, row=1)


master.mainloop()
