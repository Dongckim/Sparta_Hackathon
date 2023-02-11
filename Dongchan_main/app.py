from flask import Flask, render_template, jsonify,request
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.fl8pcqp.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
   return render_template('main.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route("/checkId", methods=["GET"])
def checkId_get():
    users_list = list(db.users.find({}, {'_id': False}))
    return jsonify({'users': users_list})

@app.route("/create", methods=["POST"])
def create_post():
    name_receive = request.form["give_name"]
    id_receive = request.form["give_id"]
    pw_receive = request.form["give_pw"]

    doc = {
        'userName':name_receive,
        'userId': id_receive,
        'userPw': pw_receive,
        'postName ': None,
        'postContent ': None,
        'supportAmount ': None
    }
    db.users.insert_one(doc)
    return jsonify({'msg': '가입완료되엇습니다'})

@app.route("/support", methods=["GET"])
def support_get():
    user_list = list(db.users.find({}, {'_id': False}))
    return jsonify({'users': user_list})

@app.route("/main", methods=["GET"])
def modal_get():
    user_list = list(db.users.find({}, {'_id': False}))
    return jsonify({'users':user_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)


