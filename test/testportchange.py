import serial
import serial.tools.list_ports

sr = serial.tools.list_ports.comports()
oldsr = sr
for port in sr:
    print(f"oldsr{port}")
while sr == oldsr:
    sr = serial.tools.list_ports.comports()
print("change")
for port in sr:
    print(f"newsr{port}")
