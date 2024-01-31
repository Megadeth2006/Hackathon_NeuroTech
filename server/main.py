from flask import Flask, jsonify, request, abort
from json import loads, dumps
from flask_cors import CORS, cross_origin
from collections import deque
import time
from db import DB
import midlware as mdw
from mailer import Emailer
from hashing import *
import music


print('Starting server...')

music.main()
db = DB()
db.create_db()
emailer = Emailer()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

ip_queue = {}

max_requests = 120
interval = 60

def is_allowed(ip):
    if ip not in ip_queue:
        ip_queue[ip] = deque([time.time()], maxlen=max_requests)
    else:
        ip_queue[ip].append(time.time())
        if (
            len(ip_queue[ip]) == max_requests
            and ip_queue[ip][-1] - ip_queue[ip][0] < interval
        ):
            return False
    return True

@app.before_request
def limit_requests():
    if not is_allowed(request.remote_addr):
        return (
            jsonify({"error": "Too many requests"}),
            429,
            {"Content-Type": "application/json"},
        )
    
@app.route("/registration", methods=['POST'])
def registration():
    if request.method == "POST":
        try:
            try:
                form = request.form
            except:
                form = loads(request.data.decode('utf-8'))
            name = form["name"]
            lastname = form["lastname"]
            email = form["email"]
            password = calculate_sha(form["password"])
            mail_active = mdw.generate_name_files(40)
            res = db.registration(name, lastname,password, email,  mail_active)
            if res:
                emailer.confirmation_by_email(email, mail_active)
            return jsonify({'id' : bool(res)})
        except Exception as e:
            print(e)
            abort(404)

@app.route("/check", methods=['POST'])
def check():
    if request.method == "POST":
        try:
            try:
                form = request.form
            except:
                form = loads(request.data.decode('utf-8'))
            email = form["email"]
            password = calculate_sha(form["password"])
            res = db.check_credentials( email, password)
            return jsonify({'id' : res})
        except Exception as e:
            print(e)
            abort(404)

@app.route("/confirm/<mail_active>", methods=['GET'])
def confirm(mail_active):
    if request.method == "GET":
        try:
            res = db.confirm_mail(mail_active)
            return jsonify({'id' : bool(res)})
        except Exception as e:
            print(e)
            abort(404)

@app.route("/get_random_musics", methods=['GET'])
def get_random_musicse():
    if request.method == "GET":
        try:
            res = db.get_random_musics()
            path = f"static/{res[2]}-{res[3]}/{res[1]}"
            return jsonify({'id' : res,
                            'path': path})
        except Exception as e:
            print(e)
            abort(404)

@app.route("/get_all_musics", methods=['GET'])
def get_all_musicse():
    if request.method == "GET":
        try:
            res = db.get_all_musics()
            return jsonify({'id' : res})
        except Exception as e:
            print(e)
            abort(404)


@app.route("/set_musics", methods=['POST'])
def set_musicse():
    if request.method == "POST":
        try:
            try:
                form = request.form
            except:
                form = loads(request.data.decode('utf-8'))
            ids = form["id"]
            relax = form["relax"]
            consentration = form["consentration"]
            res = db.set_reta_music(int(ids), float(relax), float(consentration))
            return jsonify({'id' : bool(res)})
        except Exception as e:
            print(e)
            abort(404)

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)