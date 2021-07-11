import serial
from firebase import firebase
from time import sleep
from datetime import datetime
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port, desc, hwid))

ser = serial.Serial("COM2", 9600)
print(ser.readline())
res = 1
i = 0
time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)
a = []
str1 = str(ser.readline())
a = str1.split(",")
a_x = a[0]
a_y = a[0]
a_z = a[0]
a_x = a_x[2:]
a_y = a_y
a_z = a_z[:-5]
print(a_z)
while res:
    cc = str(1234)
    print(cc)
    val = cc
    firebase1 = firebase.FirebaseApplication('https://soundmonitor-c5f9c-default-rtdb.firebaseio.com/',
                                             None)  ##paste your firebase url

    for i in range(0, 4):
        string1 = "123"
        # string1=str(ser.readline())
        # string1=string1[9:][:-6]
        data = {'date': datetime.now().strftime("%Y-%m-%d"),
                'reading': a_x,
                'time': datetime.now().strftime("%H:%M")
                }
        result = firebase1.patch(
            'https://soundmonitor-c5f9c-default-rtdb.firebaseio.com/' + '/a_x_data/' + str(i),
            data)  ##paste your firebase url
        print(result)

    for i in range(0, 4):
        string1 = "123"
        # string1=str(ser.readline())
        # string1=string1[9:][:-6]
        data = {'date': datetime.now().strftime("%Y-%m-%d"),
                'reading': a_y,
                'time': datetime.now().strftime("%H:%M")
                }
        result = firebase1.patch(
            'https://soundmonitor-c5f9c-default-rtdb.firebaseio.com/' + '/a_y_data/' + str(i),
            data)  ##paste your firebase url
        print(result)

    for i in range(0, 4):
        string1 = "123"
        # string1=str(ser.readline())
        # string1=string1[9:][:-6]
        data = {'date': datetime.now().strftime("%Y-%m-%d"),
                'reading': a_z,
                'time': datetime.now().strftime("%H:%M")
                }
        result = firebase1.patch(
            'https://soundmonitor-c5f9c-default-rtdb.firebaseio.com/' + '/a_z_data/' + str(i),
            data)  ##paste your firebase url
        print(result)

    res = 0
