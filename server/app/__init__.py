from flask import Flask, request,render_template
from flask import jsonify
from flask_cors import CORS
import urllib.parse
from .tasks.models import db, Task


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
# Configure Database URI:
params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=testing-azure.database.windows.net;DATABASE=toDoApp;UID=agcastro1994;PWD=art041,,,")

SECRET_KEY = '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789'
#PROPAGATE_EXCEPTIONS = True
# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SHOW_SQLALCHEMY_LOG_MESSAGES'] = False
app.config['ERROR_404_HELP'] = False


if __name__ == '__main__':
    app.debug = True

#Flask REST Api code
# api = Api(app)
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()

#
# class TaskList(Resource):
#     def get(self):
#         tasks = Task.query.all()
#         return {'Tasks': list(x.json() for x in tasks)}
#
#     def post(self):
#         data = request.get_json()
#         task = Task(data['title'])
#         task.save()
#         return task.json(), 201
#
#
# class aTask(Resource):
#     def get(self, title):
#         task = Task.query.filter_by(title=title).first()
#         if task:
#             return task.json()
#         return {'message': 'task not found'}, 404
#
#     def put(self, title):
#         data = request.get_json()
#
#         task = Task.query.filter_by(title=title).first()
#
#         if task:
#             task.finished = data["finished"]
#
#         else:
#             task = Task(title=title, **data)
#
#         task.save()
#
#         return task.json()
#
#     def delete(self, title):
#         task = Task.query.filter_by(title=title).first()
#         if task:
#             task.delete()
#             return {'message':'Deleted'}
#         else:
#             return {'message': 'task not found'}, 404
#
#
# api.add_resource(TaskList, '/tasks')
# api.add_resource(aTask, '/task/<string:title>')


def get_tasks():
    tasks = Task.query.all()
    return jsonify(tasks=[t.serialize for t in tasks])


def get_task(task_id):
    task = Task.query.filter_by(id=task_id).one()
    return jsonify(task=task.serialize)


def makeANewtask(title):
    task = Task(title=title)
    task.save()
    return jsonify(Task=task.serialize)


def updateTask(id, title, finished):
    task = Task.query.filter_by(id=id).one()
    if title:
        task.title = title
    if finished:
        task.finished = finished
    task.save()
    return 'Updated a Task with id %s' % id


def deleteATask(id):
    task = Task.query.filter_by(id=id).one()
    task.delete()

    return 'Removed task with id %s' % id


@app.route('/')
@app.route('/tasks', methods=['GET', 'POST'])
def taskFunction():
    if request.method == 'GET':
        return get_tasks()
    elif request.method == 'POST':
        title = request.args.get('title', '')
        return makeANewtask(title)



@app.route('/task/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def taskFunctionId(id):
    if request.method == 'GET':
        return get_task(id)

    # revisar ...no esta funcionando
    elif request.method == 'PUT':
        title = request.args.get('title', '')
        finished = request.args.get('finished', '')
        return updateTask(id, title, finished)

    elif request.method == 'DELETE':
        return deleteATask(id)


