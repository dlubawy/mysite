import os, smtplib, urllib.request, urllib.parse, json
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from email.mime.text import MIMEText

# create our little application :)
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(__name__)
app.config.from_pyfile('development.cfg', silent=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_contact', methods=['POST'])
def _contact():
    error = None
    success = None
    if request.method == 'POST':
        if request.form['name'] == "":
            flash("No name.", "warning")
        elif request.form['email'] == "":
            flash("No email.", "warning")
        elif check_captcha(request.form['g-recaptcha-response']) == False:
            flash("Captcha not verified", "danger")
        else:
            send_msg(request.form['name'], request.form['email'], request.form['message'])
            flash("Message sent.", "success")
            return redirect(url_for("index", _anchor="contact"))
    return redirect(url_for("index", _anchor="contact"))

def check_captcha(response):
    data = {
            "secret":app.config['CAPTCHA_SECRET'],
            "response":response
            }
    url_data = urllib.parse.urlencode(data)
    url = "https://www.google.com/recaptcha/api/siteverify?" + url_data
    res = urllib.request.urlopen(url)
    read = json.loads(res.read().decode('ascii'))
    if read["success"] == True:
        return True
    return False

def send_msg(name, email, message):
    msg = name+"\n"+email+"\n"+message
    data = {
            "bot_id":app.config['BOT_ID'],
            "text":msg
            }
    req = urllib.request.Request("https://api.groupme.com/v3/bots/post", data=json.dumps(data).encode("ascii"), headers={"Content-Type":"application/json"})
    response = urllib.request.urlopen(req)
