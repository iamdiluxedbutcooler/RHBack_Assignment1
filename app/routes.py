from app import app, mongo
from flask import jsonify, request, Response

@app.route('/about_me',
           methods =  ['POST', 'GET'])
def about_me():
    if request.method == 'POST':
        data = request.get_json()
        mongo.db.users.insert_one(data)
        return Response("Entry added", status = 201)
    elif request.method == 'GET':
        name = request.args.get('name')
        user = mongo.db.users.find_one({"Name": name})
        if user:
            user.pop('_id')
            return jsonify(user)
        else:
            return Response("User not found", status = 404)
    
    #return jsonify({"Name": "Pleng Litchiowong", 
    #                "Course": "Computer Science", 
    #                "Year": "1", 
    #                "CCAs": "RHDevs, RHMP, BlkComm, WelfareComm, OCIP, RVC SN, BOP, AnG"})
