import serial
import time
import re
import sqlite3

for com in range(0,4):
  try:
    PORT = '/dev/ttyACM'+str(com)
    BAUD = 9600
    board = serial.Serial(PORT,BAUD)
    board.close()
    break
  except:
    pass

DEVICE = '/dev/ttyACM'+str(com)
BAUD = 9600

s = serial.Serial(DEVICE, BAUD, timeout=3)
time.sleep(5) # der Arduino resettet nach einer Seriellen Verbindung, daher muss kurz gewartet werden

def send_and_receive( theinput ):
    s.write( theinput )
    while True:
        try:
            time.sleep(0.01)
            line = s.readline()
            return line
        except:
            pass
    time.sleep(0.1)

while True:
    response = send_and_receive('1')
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", response)
    print(numbers)
    if len(numbers) == 6:
            temp = numbers[3]
            ec = numbers[1]
            light = float(numbers[4])
            moisture = numbers[5]
            # datetime('now','localtime')
    time.sleep(300)
