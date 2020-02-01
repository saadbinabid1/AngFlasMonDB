from bson import ObjectId
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'meantask'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/meantask'

mongo = PyMongo(app)
CORS(app)


@app.route('/api/tasks', methods=['GET'])
def get_all_tasks():
    tasks = mongo.db.tasks
    result = []
    for field in tasks.find():
        result.append({'_id': str(field['_id']), 'title': field['title'], 'status': field['status']})
    return jsonify(result)


@app.route('/api/task', methods=['POST'])
def add_task():
    tasks = mongo.db.tasks
    title = request.get_json()['title']
    response = tasks.find_one({'title': title})
    task_id = tasks.insert([{'title': title, 'status': 'not done'}])
    new_task = tasks.find_one({'_id': task_id})
    result = {'title': new_task['title'], 'status': new_task['status']}
    return jsonify({'result': result})


@app.route('/api/task/<id>', methods=['PUT'])
def update_task(id):
    tasks = mongo.db.tasks
    title = request.get_json()['title']
    id = request.get_json()['_id']
    status = request.get_json()['status']

    tasks.find_one_and_update({'_id': ObjectId(id)}, {'$set': {'title': title, 'status': status}}, upsert=False)
    new_task = tasks.find_one({'_id': ObjectId(id)})
    result = [{'title': new_task['title'], 'status': new_task['status']}]

    return jsonify({'result': result})


@app.route('/api/task/<id>', methods=['DELETE'])
def delete_task(id):
    tasks = mongo.db.tasks
    new_task = tasks.find_one({'_id': ObjectId(id)})
    title= new_task['title']

    tasks.find_one_and_update({'_id': ObjectId(id)}, {'$set': {'title': title, 'status': 'done'}}, upsert=False)
    result = [{'title': title, 'status': 'done'}]
    # response = tasks.delete_one({'_id': ObjectId(id)})
    #
    # if response.deleted_count == 1:
    #     result = {'message': ' record deleted'}
    # else:
    #     result = {'message ': "cannot find record to delete"}

    return jsonify({'result': result})


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return message
    #  return '<h1> Error 404!</h1>' \


#         '<h2>  <a href="./">Back!</a></h2>'

@app.errorhandler(500)
def not_found(error=None):
    message = {
        'status': 500,
        'message': 'Not Found: ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 500
    return message


if __name__ == "__main__":
    app.run(debug=True)
