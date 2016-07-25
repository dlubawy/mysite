import os, smtplib
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from email.mime.text import MIMEText

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY='dc3919eb32e433499beefaeb7509297542faa2729c81bb4c89e14699ee759995'
    ))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    error = None
    success = None
    if request.method == 'POST':
        if request.form['name'] == "":
            flash("No name.", "warning")
        elif request.form['email'] == "":
            flash("No email.", "warning")
        else:
            send_msg(request.form['name'], request.form['email'], request.form['message'])
            flash("Message sent.", "success")
            return redirect("http://127.0.0.1:5000/#contact")
    return redirect('http://127.0.0.1:5000/#contact')

def send_msg(name, email, message):
    msg = MIMEText(message)
    msg['From'] = email
    msg['To']  = "dlubawy@gmail.com"
    msg['Subject'] = name

    # The actual mail send
    server = smtplib.SMTP('smtp-relay.gmail.com:25')
    server.starttls()
    server.ehlo(email)
    server.quit()  
