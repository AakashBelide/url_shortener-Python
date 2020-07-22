from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import shortuuid
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/base.db'
app.config['SECRET_KEY'] = 'hfcgvnbmnhbj'

db = SQLAlchemy(app)

class URLS(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String(25526526577))
    shortuid = db.Column(db.String(5456))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<url_id>')
def url_id(url_id):
    check_url = URLS.query.filter_by(shortuid = url_id).first()
    if check_url:
        return redirect(check_url.url)
    else:
        return "Invalid Url"

@app.route('/processor', methods = ['POST'])
def pro():
    urlid = shortuuid.ShortUUID().random(length=4)
    url = request.form['url']
    new_link = urlid
    new_url = URLS(url=url, shortuid=urlid)
    db.session.add(new_url)
    db.session.commit()
    return 'Your new url is http://127.0.0.1:5000/' + new_link

if __name__ == "__main__":
    app.run(debug = True)