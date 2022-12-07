import serial.tools.list_ports
import random
import time
import sys
from Adafruit_IO import MQTTClient

AIO_FEED_ID = ""
AIO_USERNAME = ""
AIO_KEY = ""

def connected(client):
    print("Ket not thanh cong..")
    client.subscribe(AIO_FEED_ID)

def subscribe(client, userdata, mide, granted_qos):
    print("Subscribe thanh cpng...")

def disconnected(client):
    print("Ngat ket noi...")
    sys.exit(1)

def message(client, feed_id, payload):
    print("Nhan du lieu: " + payload)
    ser.write((str(payload) + '#').encode())

client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subsribe = subscribe
client.connect()
client.lopp_background()

def getPrt():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Deviec" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort

ser = serial.Serial(port = getPort(), baudrate = 115200)

mess= ""

def processData(data):
    data = data.replace ("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitDat[1] == "TEMP":
        client.publish("bbc-temp", splitDat[2])

mess = ""
def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.finde("!")
            end = mess.find("#")
            processData(mess[start:end +1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end + 1:]

while True:
    readSerial()
    time.sleep(1) 