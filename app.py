#!/usr/bin/env python3
from flask import Flask, jsonify
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok"})

@app.route('/count', methods=['GET'])
def count():
    count = cache.incr('hits')
    return jsonify({"count": count})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
