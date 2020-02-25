from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:akash12345@localhost/codingblog'
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
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

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
    return render_template('contact.html')

@app.route('/post')
def post():
    return render_template('post.html')

if __name__ == "__main__":
    app.run()    
    db.create_all()



