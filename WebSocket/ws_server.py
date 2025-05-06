from flask import Flask, render_template
from flask_socketio import SocketIO
import random
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def send_sensor_data():
    while True:
        suhu = round(random.uniform(25.0, 35.0), 2)
        socketio.emit('sensor_data', {'suhu': suhu})
        time.sleep(2)

# Jalankan thread untuk kirim data otomatis
threading.Thread(target=send_sensor_data, daemon=True).start()

if __name__ == '__main__':
    socketio.run(app, debug=True)