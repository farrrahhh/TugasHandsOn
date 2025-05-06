# mqtt_subscriber.py
import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"
port = 1883
topic = "reksti/suhu"

def on_connect(client, userdata, flags, rc):
    print("[Subscriber] Terhubung ke broker")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"[Subscriber] Menerima dari {msg.topic}: {msg.payload.decode()} °C")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)
client.loop_forever()