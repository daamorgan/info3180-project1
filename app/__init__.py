from flask import Flask
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER='./app/static/uploads'
app=Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['SECRET_KEY']="Xz9am$hu7gry"
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_URL='postgresql://xpeuypmwyhyqsm:728951833892fd09ed749c2f690ce5e019babf1562029251c67041df607ad8ed@ec2-18-210-51-239.compute-1.amazonaws.com:5432/db2a5hquhv9oot' #"postgres://project1:password123@localhost/project1" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

app.config.from_object(__name__)
from app import views, models