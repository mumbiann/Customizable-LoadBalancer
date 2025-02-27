from flask import Flask
from uhashring import HashRing
import os
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    server_id = os.environ.get('SERVER_ID', 'Unknown')
    return f'Hello from Server: {server_id}\n'

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    # Sends empty response with a valid response code (200 OK)
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
