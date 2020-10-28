from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__) 

@app.route("/") 
def home_view(): 
		return render_template('index.html', data= getData())

ENV = 'Prod'

if ENV == 'dev':
	app.debug = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:nav123@localhost/hpractice'
else:
	app.debug = False
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://rdgdiyitwifysu:e4d0e37b0fa620047fafa6d0b7c2dc4430f1d4d79ab6ed9b446c1d9ab08c1a1d@ec2-3-216-92-193.compute-1.amazonaws.com:5432/d1a5g4oubn8icf'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Expenditure(db.Model):
	__tablename__ = 'expenditure'
	Description = db.Column(db.String(200), primary_key=True)
	Expenditure = db.Column(db.Integer)
	def __init__(self, description, expenditure):
		self.Description = description
		self.Expenditure = expenditure

def getData():
	data = Expenditure.query.all()
	rowlist = []
	for row in data:
		tmap = {
			row.Description.strip(): row.Expenditure
		}
		rowlist.append(json.dumps(tmap))
	return json.dumps(rowlist)

if __name__ == "__main__": 
	app.run() 
