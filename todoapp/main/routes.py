from flask import Blueprint, render_template, redirect, url_for, request
from bson.objectid import ObjectId
from todoapp.extensions import mongo
main = Blueprint('main', __name__)

@main.route('/')
def index():
    todos_collection = mongo.db.todos
    todos = todos_collection.find()
    return render_template('index.html', todos = todos)


@main.route('/add_todo', methods=['GET', 'POST'])
# Note - must add the GET method when using POST, in line above.
def add_todo():
    todo_item = request.form.get('add-todo')
    print(todo_item)
    todos_collection = mongo.db.todos
    todos_collection.insert_one({'text' : todo_item, 'complete': False})
    return redirect(url_for('main.index'))


@main.route('/complete_todo/<oid>')
def complete_todo(oid):
    todos_collection = mongo.db.todos
    todo_item = todos_collection.find_one({'_id' : ObjectId(oid)})
    todo_item['complete'] = True
    todos_collection.save(todo_item)
    return redirect( url_for('main.index'))