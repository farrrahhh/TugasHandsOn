# mqtt_publisher.py
import paho.mqtt.client as mqtt
import time
import random

broker = "test.mosquitto.org"
port = 1883
topic = "reksti/suhu"

client = mqtt.Client()
client.connect(broker, port, 60)

# Kirim 5 data suhu
for i in range(5):
    suhu = round(random.uniform(25.0, 35.0), 2)
    message = f"{suhu}"
    client.publish(topic, message)
    print(f"[Publisher] Mengirim suhu: {message} °C")
    time.sleep(1)

client.disconnect()