import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import fun
from db import connection

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db=SQLAlchemy(app)
class Student(db.Model):
    __tablename__='student'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    marks=db.Column(db.Integer)

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks


@app.route('/student',methods=['POST'])
def add_student():
    name=request.json['name']
    marks=request.json['marks']
    s=Student(name,marks)
    db.session.add(s)
    db.session.commit()

    data={
        "message":"data recived",
        "data":{
            "name":s.name,
            "marks":s.marks,
            "id":s.id
        }
    }
    return jsonify(data),201

create_table_query = """
CREATE TABLE officers (
    officer_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    post VARCHAR(255),
    dist VARCHAR(255),
    dept VARCHAR(255)
)
"""
conn=connection()
cur=conn.cursor()

@app.route('/create_table_officers',methods=['GET'])
def create_table():
    cur.execute(create_table_query)
    conn.commit()
    data={
        "message":"table created"
    }

    cur.close()
    conn.close()

    return jsonify(data),201

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/sum')
def sum():
   a=request.get_json()['a']
   b=request.get_json()['b']
   c=fun.sum(a,b)
   return jsonify(c),200

@app.route('/avg/<int:a>/<int:b>')
def avg(a,b):
    c=fun.avg(a,b)
    return jsonify({"message":"data recived","data":c}),200


@app.route('/armstrong')
def armstrong():
    n=request.args['n']
    n=int(n)
    c=fun.armstrong(n)
    return jsonify(c),200

@app.route('/greet')
def greet():
    name=request.form['name']
    c=fun.greet(name)
    return jsonify(c),200


if __name__ == '__main__':
    app.run(debug=True)