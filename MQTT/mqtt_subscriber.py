import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected to broker!")
        client.subscribe("web_topic")
    else:
        print(f"Connection failed! Code: {reason_code}")

def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Subscriber_V2")
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect("localhost", 1883)
    client.loop_forever()
except ConnectionRefusedError:
    print("\nERROR: Broker tidak aktif!")
    print("1. Pastikan Mosquitto sudah diinstall")
    print("2. Jalankan broker di terminal: mosquitto -v")
except KeyboardInterrupt:
    print("\nSubscriber dihentikan")