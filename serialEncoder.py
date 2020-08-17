import numpy as np
import serial
import time
import struct

try:
   ser = serial.Serial("COM6", 115200, timeout = 1)
   print(f"serial upen? {ser.isOpen()}")
except:
   print("serial error")

i = 0
while True:
   message=[]
   for i in range(8):
      tmp = ser.read(4)
      tmp = struct.unpack('f', tmp)
      message.append(tmp)
      
   print(f"{message}\n")
   time.sleep(0.035)