from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

import requests
from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.fl8pcqp.mongodb.net/?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.dbsparta

@app.route('/', methods=["GET"])
def home():
    return render_template('main.html')

@app.route("/main", methods=["GET"])
def modal_get():
    user_list = list(db.users.find({}, {'_id': False}))
    return jsonify({'users':user_list})

# @app.route("/main", methods=["GET"])
# def modal_total_get():
#     user_list = list(db.users.find({}, {'_id': False}))
#     asum = 0
#     for i in user_list:
#         asum += i['supportAmount']
#     # print(asum)
#     return jsonify({'result':asum})


# 회원가입 db insert
# user_list = list(db.users.find({}, {'_id': False}))
# num = len(user_list) + 1
# doc = {
#     'num': num,
#     'userName': '웹에서 받은 receive변수',
#     'userId': '웹에서 받은 receive변수',
#     'userPw': '웹에서 받은 receive변수',
# }
# print(db.users.insert_one(doc))

# 게시판 작성 db insert
# doc = {
#     'postName': '웹에서 받은 receive변수',
#     'postContent': '웹에서 받은 receive변수',
# }
# print(db.users.insert_one(doc))

# 후원금액 db insert
# doc = {
#     'supportAmount': '웹에서 받은 receive변수',
#     'postContent': '웹에서 받은 receive변수',
# }
# print(db.users.insert_one(doc))


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)