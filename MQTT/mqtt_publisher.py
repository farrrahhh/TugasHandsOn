from flask import Flask, request, render_template
import paho.mqtt.publish as publish

app = Flask(__name__)
broker = "localhost"
port = 1883
topic = "web_topic"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        try:
            # Kirim pesan ke broker lokal
            publish.single(
                topic, 
                message, 
                hostname=broker, 
                port=port
            )
            return render_template('/index.html', status=f"Sent: {message}")
        except Exception as e:
            return render_template('/index.html', status=f"Error: {str(e)}")
    
    return render_template('index.html', status="Ready")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)