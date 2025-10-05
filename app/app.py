from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

http_errors = Counter('http_server_requests_errors_total', 'Number of HTTP errors')

@app.route('/')
def home():
    return "Hello from Flask on AKS with Prometheus!"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
