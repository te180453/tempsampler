import serial
import time
from serial.tools import list_ports
import requests

ports = list_ports.comports()
for info in ports:
    print(info.device)
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.1) 
while True:
    try:
        adc = ser.read_all()
        if adc != b"":
            temp = str(int(float(adc.decode().replace("\r\n",""))))
            requests.get(f"http://192.168.1.111:8000/{temp}")
            print(temp)
    except Exception as e:
        print(e)
    time.sleep(1)
ser.close()