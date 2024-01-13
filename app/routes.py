from app import app
from flask import jsonify

@app.route('/')
def home():
    return "Hello Backend"

@app.route('/about_me',
           methods =  ['POST'])
def about_me():
    return jsonify({"Name": "Pleng Litchiowong", 
                    "Course": "Computer Science", 
                    "Year": "1", 
                    "CCAs": "RHDevs, RHMP, BlkComm, WelfareComm, OCIP, RVC SN, BOP, AnG"})
