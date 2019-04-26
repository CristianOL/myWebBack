
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})
app.config['DEBUG'] = True;
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/linkedIn'
app.config['SQLALCHEMY_ECHO'] = False 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'secretkey'

db = SQLAlchemy(app)

# Define the table:
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    linkedIn = db.Column(db.String(500), unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=True, nullable=False, default=datetime.utcnow)

    # Que se muestra al printear un objeto:
    def __repr__(self):
        return '<id %r><User %r><Date %r>\n' % (self.id, self.linkedIn, self.date)

db.create_all()
db.session.commit()





