# client.py
import requests
import random
import time

url = 'http://localhost:5000/sensor'

for i in range(5):
    suhu = round(random.uniform(25.0, 35.0), 2)
    payload = {"suhu": suhu}
    response = requests.post(url, json=payload)
    print(f"[Client] Mengirim suhu: {suhu} °C")
    print(f"[Server] Respon: {response.json()}")
    time.sleep(1)