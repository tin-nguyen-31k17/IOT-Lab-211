import sysfrom Adafruit_IO import MQTTClient

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

client = MQTTClient(AIO_USERNAME, AIO_KEY)