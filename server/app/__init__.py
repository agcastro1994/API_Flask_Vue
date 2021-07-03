from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
import urllib.parse
from .tasks.models import db, Task


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
# Configure Database URI:
params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=testing-azure.database.windows.net;DATABASE=toDoApp;UID=agcastro1994;PWD=art041,,,")

SECRET_KEY = '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789'
PROPAGATE_EXCEPTIONS = True

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SHOW_SQLALCHEMY_LOG_MESSAGES'] = False
app.config['ERROR_404_HELP'] = False


if __name__ == '__main__':
    app.debug = True

db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()

# Funciones de CRUD API


# Trae todas las tareas y convierte la lista en JSON
def get_tasks():
    tasks = Task.query.all()
    return jsonify(tasks=[t.serialize for t in tasks])


# Trae una tarea y la  convierte en JSON

def get_task(task_id):
    task = Task.query.filter_by(id=task_id).one()
    return jsonify(task=task.serialize)


# Crea una tarea con el titulo que se recibe desde el FrontEnd
def makeANewtask(title):
    task = Task(title=title)
    task.save()
    return jsonify(Task=task.serialize)


# Actualiza una tarea con el titulo y el estado que se recibe desde el FrontEnd
def updateTask(id, edit_info):
    task = Task.query.get(id)
    for title, finish in edit_info.items():
        setattr(task, title, finish)
    task.save()
    return 'Updated a Task with id %s' % id

# Borra una tarea identificandola con su id
def deleteATask(id):
    task = Task.query.filter_by(id=id).one()
    task.delete()

    return 'Removed task with id %s' % id


@app.route('/')
@app.route('/tasks', methods=['GET', 'POST'])
def taskFunction():
    # Recibe la solicitud GET para mostrar toda la lista
    if request.method == 'GET':
        return get_tasks()
    # Si la solicitud es un post, toma el titulo e invoca al creador de tareas
    elif request.method == 'POST':

        title = request.get_json()

        return makeANewtask(title['title'])


@app.route('/task/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def taskFunctionId(id):
    # Recibe la solicitud GET para mostrar una tarea

    if request.method == 'GET':
        return get_task(id)
    # Si  la solicitud es un put, toma los valores recibidos e invoca al editor
    elif request.method == 'PUT':
        edit_info = request.get_json()
        return updateTask(id, edit_info)
    # Si la solicitud es delete, invoca al eliminador de tareas
    elif request.method == 'DELETE':
        return deleteATask(id)


