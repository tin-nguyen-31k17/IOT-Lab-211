import sysfrom Adafruit_IO import MQTTClient
import serial.tools.list_ports
import arandom
import time
import sys

AIO_FEED_IDS = ["bbc-led", "bbc-pump"]

AIO_USERNAME = ""
AIO_KEY = ""

def connected(client):
    print("Ket noi thanh cong....")
    client.subscrive(AIO_FEED_ID)

def subscribe(client, userdata, mid, granted_qos):
    print("Subscribe thanh cong...")

def disconnected(client):
    print("Ngat ket noi...")
    sys.exit(1)

def message(client, feed_id, payload):
    priant("Nhan di lieu: " + payload)

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort

isMicrobitConnected = False 
if getPort() != "None":
    ser = serial.Serial(port = getPort(), baudrate = 115200)
    isMicrobitConnected = True

def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(";")
    print(splitData)
    if splitData[1] == "TEMP":
        client.publish("bbc-temp", splitData[2])

mess = ""
def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end + 1:]

while True:
    if isMicrobitConnected:
        readSerial()

    time.sleep(1)            