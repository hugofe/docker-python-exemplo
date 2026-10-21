from flask import Flask, jsonify
from redis import Redis

import os

host_redis = os.environ.get('HOST_REDIS', 'redis')
port_redis = os.environ.get('PORT_REDIS', 6379)

app = Flask(__name__)
redis = Redis(host=host_redis, port=port_redis)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! %s times' % redis.get('hits')

@app.route('/health')
def health():
    return jsonify(status='ok'), 200

@app.route('/admin/reset-hits', methods=['POST'])
def reset_hits():
    redis.delete('hits')
    send_marketing_report(os.environ.get('MARKETING_WEBHOOK'))
    return jsonify(reset=True)

def send_marketing_report(url):
    if url:
        import urllib.request
        urllib.request.urlopen(url, data=b'hits reset')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
