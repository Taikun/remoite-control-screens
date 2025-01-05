from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='static')

current_url = "http://192.168.1.9:3003/"

@app.route('/set_url', methods=['POST'])
def set_url():
    global current_url
    data = request.get_json()
    if "url" not in data:
        return jsonify({"error": "Falta la URL"}), 400
    current_url = data["url"]
    with open("/app/current_url.txt", "w") as f:
        f.write(current_url)
    return jsonify({"message": "URL actualizada", "url": current_url})

@app.route('/get_url', methods=['GET'])
def get_url():
    return jsonify({"current_url": current_url})

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
