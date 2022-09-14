import string
import random
from flask import render_template, redirect, url_for, request, session, Flask, jsonify
from functools import wraps

from exts import db
from config import Config
from models import *
from forms import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config.from_object(Config)
app.config['MYSQL_LOCAL_INFILE'] = True
db.init_app(app)


@app.route('/')
@app.route('/index')
def index():
    print(f"[*][*]{request.remote_addr} request /index")
    return render_template('index.html', title='12019054A', requestIp=request.remote_addr)


@app.route('/')
@app.route('/api/ip')
def ip():
    ip = request.remote_addr
    if ip is None or ip == '':
        return jsonify(
            code=400,
            msg='ip get Err0r!',
            ip=''
        )
    return jsonify(
        code=200,
        msg='success',
        ip=ip
    )


@app.route('/api/comment', methods=["POST"])
def comment():
    print(f"[*]{request.remote_addr} request /api/comment")
    try:
        form = CreateCommentForm()
        if request.method == "POST":
            ip = form.ip.data
            videoName = form.video.data
            text = form.text.data
            if ip is None or videoName is None or text is None:
                print(
                    f"[*][-]{request.remote_addr} request /api/comment:\n'{ip}' comment '{videoName}': '{text}'\n[-]code 400")
                return jsonify(
                    code=400,
                    msg="bad requests",
                    result=''
                )
            import datetime
            datetimeNow = datetime.datetime.now()
            data = Comment(
                ip=ip,
                videoName=videoName,
                text=text,
                datetime=datetimeNow
            )

            db.session.add(data)
            db.session.commit()

            print(
                f"[*][+]{request.remote_addr} request /api/comment:\n'{ip}' comment '{videoName}':'{text}'\n[+]Comment success")
            return jsonify(
                code=200,
                msg="success",
                result=''
            )
        else:
            print(f"[*][-]{request.remote_addr} request /api/comment : code 500")
            return jsonify(
                code=500,
                msg="Interval Server Err0r!",
                result=''
            )
    except Exception as e:
        print(f"[*][-]{request.remote_addr} request /api/comment : code 500")
        return jsonify(
            code=501,
            msg="Interval Server Err0r!",
            result=str(e)
        )


@app.route('/api/getComments', methods=["GET"])
def getComments():
    print(f"[*]{request.remote_addr} request /api/getComments")
    try:
        videoName = request.args.get("video")
        if videoName is None:
            print(f"[*][-]{request.remote_addr} request /api/getComments : code 400")
            return jsonify(
                code=400,
                msg="bad requests",
                result=''
            )

        sql = f"select ip,datetime,text from comment where videoName='{videoName}' order by datetime desc"

        result = db.session.execute(sql, params={"multi": False})
        db.session.commit()

        result = result.fetchall()
        data = []
        for i in result:
            data.append(dict(i))
        print(f"[*][+]{request.remote_addr} request /api/getComments : success")
        return jsonify(
            code=200,
            msg="success",
            result=data
        )

    except Exception as e:
        print(f"[*][-]{request.remote_addr} request /api/getComments : code 501")
        return jsonify(
            code=501,
            msg='Interval Server Err0r!',
            result=str(e)
        )


@app.route('/api/Signin', methods=['POST'])
def signin():
    print(f"[*]{request.remote_addr} request /api/Signin")
    try:
        form = CreateSignInForm()
        if request.method == "POST":
            ip = form.ip.data
            if ip is None:
                print(f"[*][-]{request.remote_addr} request /api/Signin to sign '{ip}': code 400")
                return jsonify(
                    code=400,
                    msg="bad requests",
                    result=''
                )
            import datetime
            datetimeNow = datetime.datetime.now().strftime("%Y-%m-%d")

            sql = f"select `datetime` from signin where ip='{ip}' order by `datetime` desc"
            res = db.session.execute(sql, params={"multi": False}).fetchone()
            if res is not None:
                result = datetime.datetime.strftime(res[0], "%Y-%m-%d")
                if datetimeNow <= result:
                    print(f"[*][-]{request.remote_addr} request /api/Signin : {ip} Already Signed")
                    return jsonify(
                        code=201,
                        msg="Already Signed!",
                        result=''
                    )
            data = SignIn(ip=ip,
                          datetime=datetime.datetime.now())
            db.session.add(data)
            db.session.commit()
            print(f"[*][+]{request.remote_addr} request /api/Signin : {ip} signin success")
            return jsonify(
                code=200,
                msg="success",
                result=''
            )
        else:
            print(f"[*][-]{request.remote_addr} request /api/Signin : code 500")
            return jsonify(
                code=500,
                msg="Interval Server Err0r!",
                result=''
            )
    except Exception as e:
        print(f"[*][-]{request.remote_addr} request /api/Signin : code 500")
        return jsonify(
            code=501,
            msg="Interval Server Err0r!",
            result=str(e)
        )


@app.route('/api/getSignInUsers', methods=["GET"])
def getSignInUsers():
    print(f"[*]{request.remote_addr} request /api/getSignInUsers")
    sql = f"select ip,datetime from signin order by datetime desc"
    try:
        result = db.session.execute(sql, params={"multi": False})
        db.session.commit()

        result = result.fetchall()
        data = []
        for i in result:
            data.append(dict(i))
        return jsonify(
            code=200,
            msg="success",
            result=data
        )
    except Exception as e:
        return jsonify(
            code=501,
            msg='Interval Server Err0r!',
            result=str(e)
        )


if __name__ == '__main__':
    app.run(threaded=False, processes=100, debug=False, host='0.0.0.0', port=5000)
