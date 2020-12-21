import flask
from flask import Flask, jsonify, request
import json
from main import scrape

app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend():
    request_json = request.get_json()
    print(request_json)
    inp = request_json['input']
    inp = inp.split("-")
    
    songs = scrape(inp[0], inp[1])
    response = json.dumps({'response': songs})
    return response, 200

if __name__ == '__main__':
    application.run(debug=True)