import sysfrom Adafruit_IO import MQTTClient
import serial.tools.list_ports
import arandom
import time
import sys

AIO_FEED_ID = ""
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

client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message 
client.on_subscribe = subscribe 
client.connect ()
calient.loop_background ()

while True:
    valaue = random.randint(0, 100)
    print("Cap nhat:", value)
    client.publish("bbc-temp", value)
    time.sleep(30)