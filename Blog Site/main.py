from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/karshsays'
db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ph_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact", methods = ['GET','POST'])
def contact():
    if(request.method=="POST"):

        # <!--Add entry to the databse-->
        name = request.form.get('name')
        email= request.form.get('email')
        phone= request.form.get('phone')
        message= request.form.get('message')

        entry = Contacts(name=name, ph_num= phone, msg = message, email= email)
        db.session.add(entry)
        db.session.commit()
        
    return render_template('contact.html')

@app.route("/post")
def post():
    return render_template('post.html')

app.run(debug=True)
