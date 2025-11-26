from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dados.db"
db = SQLAlchemy()
db.init_app(app)

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)

@app.route('/')
def index():
    return 'hello world!'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)