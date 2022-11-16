from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca=certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.ryuvr6l.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('like.html')


@app.route("/api/comment", methods=["POST"])
def web_mars_post():
    nickname_receive = request.form['nickname_give']
    comment_receive = request.form['comment_give']


    doc = {
        'nickname': nickname_receive,
        'comment': comment_receive,


    }
    db.athumb.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})


@app.route("/api/comment", methods=["GET"])
def web_athumb_get():
    order_list = list(db.athumb.find({}, {'_nickname': False}))
    return jsonify({'orders':order_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
