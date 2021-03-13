from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:nelsonkimathi123@localhost:5432/test254'
db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all

class Nelson(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), unique=True, nullable=False)
    lname = db.Column(db.String(80), unique=True, nullable=False)
    email_address = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form['first_name']
        lname = request.form['last_name']
        email_address = request.form['email_address'] 

        print(fname, lname, email)
        detail = Nelson(fname = fname, lname = lname, email_address = email_address)
        print('Record successfully added')
        db.session.add(detail)
        db.session.commit()
        return redirect(url_for("register"))
    else:
        details = Nelson.query.all()
        return render_template("sample.html", details=details)

if __name__=="__main__":
    app.run(debug=True)