from config import APIKEY
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    url = f'https://newsapi.org/v2/everything?q=keyword&apiKey={APIKEY}'
    req = requests.get(url)
    if req.status_code >= 400:
        return 'Ocorreu um erro'
    responseJs = req.json()['articles']
    data = []
    for value in responseJs:
        data.append({"author": value['author'],  "title": value["title"],  "description": value["description"],})
    return jsonify(data), 200

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)