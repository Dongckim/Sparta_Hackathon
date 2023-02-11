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

@app.route('/loginPage')
def logIn():
        return render_template('login.html')

@app.route('/signupPage')
def signUp():
   return render_template('signup.html')

@app.route("/postPage")
def post():
    return render_template('post.html')




@app.route("/checkId", methods=["GET"])
def checkId_get():
    users_list = list(db.users.find({}, {'_id': False}))
    return jsonify({'users': users_list})



@app.route("/login", methods=["POST"])
def login_user():
        id_receive = request.form["id_give"]
        pw_receive = request.form["pw_give"]

        user_list = list(db.users.find({}, {'_id': False}))
        print(user_list)

        for i in user_list:
                userID = i["userId"]
                userPw = i["userPw"]
                if id_receive == '' or pw_receive == '' or id_receive == None or pw_receive == None:
                        return jsonify({'msg': 'Please provide a user name and a password.'})
                # if userID != id_receive and userPW == pw_receive:
                #         return jsonify({'msg':'The user name and password combination you entered does not correspond to a registered user.'})
                # if userID == id_receive and userPW != pw_receive:
                #         return jsonify({'msg':'The user name and password combination you entered does not correspond to a registered user.'})
                if userID == id_receive and userPw == pw_receive:
                        return jsonify({'msg':'successfully logged in'})
                # if userID != id_receive or userPw != pw_receive:
        return jsonify({'msg':'The user name and password combination you entered does not correspond to a registered user.'})





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
        'supportAmount ': 0
    }
    db.users.insert_one(doc)
    return jsonify({'msg': 'Sign Up Success'})


@app.route("/support", methods=["GET"])
def support_get():
    user_list = list(db.users.find({}, {'_id': False}))
    return jsonify({'users': user_list})


@app.route("/post", methods=["POST"])
def web_post():
    postName_ricevie = request.form['form_give']
    postContent_ricevie = request.form['input_give']

    db.users.update_one({'postName': postName_ricevie}, {'$set': {'postContent': postContent_ricevie}})
    return jsonify({'msg': '등록 완료!'})

@app.route("/get", methods=["GET"])
def post_get():
    memo_list = list(db.users.find({}, {'_id': False}))

    return jsonify({'memo': memo_list})







@app.route("/main_modal", methods=["GET"])
def modal_main():
    # user_list = list(db.users.find({},{'_id':False}))
    user_list = list(db.users.find({},{'_id':False}).sort("supportAmount"))[::-1]
    # print(user_list)
    return jsonify({'users': user_list})

@app.route("/main_search", methods=["GET"])
def modal_main_search():
    # user_list = list(db.users.find({},{'_id':False}))
    user_list = list(db.users.find({},{'_id':False}).sort("supportAmount"))[::-1]
    # print(user_list)
    return jsonify({'users': user_list})

@app.route("/main_search_new", methods=["GET"])
def modal_main_search_new():
    # user_list = list(db.users.find({},{'_id':False}))
    user_list = list(db.users.find({},{'_id':False}).sort("supportAmount"))[::-1]
    # print(user_list)
    return jsonify({'users': user_list})


@app.route("/support_btn", methods=["POST"])
def support_create():
    id_receive = request.form["id_give"]
    pw_receive = request.form["pw_give"]
    amount_receive = request.form["amount_give"]
    user_list = list(db.users.find({}, {'_id': False}))

    for i in user_list:
        if id_receive == i['userId'] and pw_receive == i['userPw']:
            amount_receive_sum = i['supportAmount'] + int(amount_receive)
            db.users.update_one({'userId': id_receive}, {'$set': {'supportAmount': amount_receive_sum}})
            return jsonify({'msg': '후원 완료!!!'})

    return jsonify({'msg': '정보를 입력하세요.'})

@app.route("/main", methods=["GET"])
def modal_get():
    user_list = list(db.users.find({}, {'_id': False}))
    return jsonify({'users':user_list})




if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)


