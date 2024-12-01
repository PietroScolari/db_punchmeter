from flask import Flask, request
import requests
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_info')
def get_info():
    headers = {
      "Content-Type": "application/json",
      "api-key": os.environ["API_KEY"]
    }
    url = "https://data.mongodb-api.com/app/data-wlaoj/endpoint/data/v1/action/find"
    body = {"collection": "cose", "database": "db1", "dataSource": "Cluster0"}
    r = requests.post(url, headers=headers, json=body)
    top = r.json()['documents']
    top.sort(reverse=True, key=sort_by_points)
    del top[100:]
    return top
  
@app.route("/add", methods=["POST"])
def add():
    headers = {
      "Content-Type": "application/json",
      "api-key": os.environ["API_KEY"]
    }
    data = request.get_json()
    print(data)
    if data['points'] > 50:
      print("QUA QUALCUNO BARA")
    else:
      url = "https://data.mongodb-api.com/app/data-wlaoj/endpoint/data/v1/action/insertOne"
      body = {"collection": "cose", "database": "db1", "dataSource": "Cluster0", 
              "document": data
             }
      r = requests.post(url, headers=headers, json=body)
      r.json()
    return data
      
def sort_by_points(e):
  return e['points']

app.run(host='0.0.0.0', port=81)