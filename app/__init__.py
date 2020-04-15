from flask import Flask
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER='./app/static/uploads'
app=Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['SECRET_KEY']="Xz9am$hu7gry"
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_URL="postgres://project1:password123@localhost/project1" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

app.config.from_object(__name__)
from app import views, models