import flask
from flask import Flask, jsonify, request
import json
from main import scrape

app = Flask(__name__)

@app.route('/recommendmusic', methods=['GET'])
def find_sims():
    request_json = request.get_json()
    print(request_json)
    inp = request_json['input']
    inp = inp.split("-")
    
    res = scrape(inp[0], inp[1])
    response = json.dumps({'response': res})
    return response, 200

if __name__ == '__main__':
    application.run(debug=True)