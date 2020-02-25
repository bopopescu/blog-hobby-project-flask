from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
from datetime import datetime
import json

with open ('config.json',mode="r") as c:
    params = json.load(c)["params"]

app = Flask(__name__)

if params["local_server"]:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]

db = SQLAlchemy(app)


# define class for database ORM
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    phone_num = db.Column(db.String(12))
    msg = db.Column(db.String(120))
    date = db.Column(db.String(120))
    email = db.Column(db.String(20))

    def __repr__(self):
        return '<User %r>' % self.username





@app.route('/')
def home():
    return render_template('index.html',params=params)

@app.route('/about')
def about():
    return render_template('about.html',params=params)

@app.route('/contact', methods = ['GET','POST'])
def contact():
    # add value to db
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name,phone_num=phone,msg=message,date=datetime.now(),email=email)
        db.session.add(entry)
        db.session.commit()
        print("Phase 5")
        print("\n\n")
    return render_template('contact.html',params=params)

@app.route('/post')
def post():
    return render_template('post.html',params=params)

if __name__ == "__main__":
    app.run(debug=True)    
    db.create_all()



