import serial
import numpy as np
import math
import struct
import matplotlib.pyplot as plt
import binascii

import matplotlib.pyplot as plt

ser = serial.Serial('COM19', 115200)

SPEED_OF_LIGHT  = 299792458
frequency = 16000000

rawFrame = []

diff_list = []

times = 10
iteration = 0
#while iteration < times:
while True:
    byte  = ser.read(1)        
    rawFrame += byte
    if rawFrame[-4:] == [13,10,13,10]:
        if rawFrame[:6] == [43,85,85,68,70,58]:
            data = rawFrame
            data = bytes(rawFrame[6:-4])
            data_str = data.decode('UTF-8')
            data_list = data_str.split(',')
            print(data_list)
            tag_id = data_list[0]
            rssi = np.float32(data_list[1])
            angle1 = np.float32(data_list[2])
            angle2 = np.float32(data_list[3])
            channel = np.int32(data_list[5])
            anchor_ID = data_list[6]
            timestamp = data_list[8]
            print('tag_id = ', tag_id)
            print('rssi = ', rssi)
            print('angle1 = ', angle1)
            print('angle2 = ', angle2)
            print('channel = ', channel)
            print('anchor_ID = ', anchor_ID)
            print('timestamp = ', timestamp)
        rawFrame = []
