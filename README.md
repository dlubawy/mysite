#MySite

##About
This is my personal website which I built after being convinced to buy my 
name's domain name. Figured it shouldn't stay empty. Very basic, built it from 
[Bootstrap](http://getbootstrap.com/) then expanded to using 
[Flask](http://flask.pocoo.org/) when I exceeded the scope of a static website 
with my contact form. I used Flask because it is a microframework and I learned 
my lesson using Django on a small app for a previous project. I used GroupMe as 
the method for sending a message because I don't have access to an email relay 
and this seemed like an easy, yet reliable solution.

##Usage
Use `git clone https://github.com/dlubawy/mysite.git` to clone the repo.  Then 
`cd mysite`. Use `pip -r requirements.txt` to install dependencies. Change 
whatever you want and setup your environment with `export FLASK_APP=mysite.py`.  
Finally run the app `flask run`.
