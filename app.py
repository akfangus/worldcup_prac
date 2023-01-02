from flask import Flask, render_template, request, jsonify
import requests

from pymongo import MongoClient
client = MongoClient('mongodb+srv://lee:sparta@Cluster0.nw7w0pd.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route("/resultlist", methods=["GET"])
def resultlist_get():
    group = request.args.get('group')

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # url_receive = 'https://fixturedownload.com/feed/json/fifa-world-cup-2022/'
    # data = requests.get(url_receive, headers=headers)
    # matches = data.json()
    group_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    # for item in group_list:
    #     all_users = list(db.matches.find({'Group': f'Group {item}'}, {'_id': False}))

    throw_matches = list(db.matches.find({'Group': f'Group {group}'}, {'_id': False}))




    # print(ns)
    # bucket_list = list(db.bucket.find({}, {'_id': False}))
    return jsonify({'throw_matches': throw_matches})


if __name__ == '__main__':
    app.run(debug=True)
