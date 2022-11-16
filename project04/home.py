from flask import Flask, render_template, request, jsonify

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://coy:sparta@cluster0.apdwkr3.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/post')
def post():
    return render_template('post.html')



@app.route("/post", methods=["POST"])
def posting():
    image_receive = request.form['image_give']
    brand_receive = request.form['brand_give']
    option_receive = request.form['option_give']
    title_receive = request.form['title_give']
    star_receive = request.form['star_give']
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    doc = {
        'image':image_receive,
        'brand':brand_receive,
        'option':option_receive,
        'title':title_receive,
        'star':star_receive,
        'url':url_receive,
        'comment':comment_receive
    }
    db.athumb.insert_one(doc)

    return jsonify({'msg': '작성 완료!'})


@app.route('/', methods=["GET"])
def post_get():
    post_list = list(db.athumb.find({}, {'_id': False}))
    return jsonify({'post_list':post_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5003, debug=True)