import serial
import time
import re
import requests

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
print("Start Serial Session")

def send_and_receive( theinput ):
    s.write( theinput )
    while True:
        try:
            time.sleep(0.01)
            line = s.readline()
            print(line)
            return line
        except:
            pass
    time.sleep(0.1)

while True:
    response = send_and_receive('1')
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", response)
    print(numbers)
    if len(numbers) == 3:
            temp = numbers[0]
            ec = numbers[1]
            k = numbers[2]
            b_value = float(1.38) + float(k)
            url = "http://localhost:8086/write?db=hydro"
            data = ("hydroculture,host=hydroino01 temp=" + temp + ",ec=" + ec + ",k=" + k + ",b=" + b_value)
            print(data)
            try:
                r = requests.post(url, data=data)
            except:
                print('Error to send data')
    time.sleep(300)
