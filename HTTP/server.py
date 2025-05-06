# server.py
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
latest_suhu = None

# Halaman utama
@app.route('/', methods=['GET', 'POST'])
def index():
    global latest_suhu
    if request.method == 'POST':
        suhu = request.form.get('suhu')
        latest_suhu = suhu
        return render_template_string(HTML_TEMPLATE, suhu=suhu)
    return render_template_string(HTML_TEMPLATE, suhu=latest_suhu)

# Endpoint API untuk client.py
@app.route('/sensor', methods=['POST'])
def receive_data():
    global latest_suhu
    data = request.json
    suhu = data.get("suhu")
    latest_suhu = suhu
    print(f"Data diterima: Suhu = {suhu} °C")
    return jsonify({"status": "success", "message": f"Suhu {suhu} diterima"}), 200

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Monitoring Suhu</title>
</head>
<body>
    <h1>Form Input Suhu Manual</h1>
    <form method="POST">
        <label>Masukkan Suhu (°C):</label>
        <input type="number" step="0.01" name="suhu" required>
        <button type="submit">Kirim</button>
    </form>

    {% if suhu %}
        <h2>Data Terakhir Diterima:</h2>
        <p>Suhu: <strong>{{ suhu }} °C</strong></p>
    {% else %}
        <p>Belum ada data dikirim.</p>
    {% endif %}
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True, port=5000)