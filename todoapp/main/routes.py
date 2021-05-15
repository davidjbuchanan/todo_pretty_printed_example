from flask import Blueprint, render_template, redirect, url_for, request
from todoapp.extensions import mongo
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/add_todo', methods=['GET', 'POST'])
# Note - must add the GET method when using POST, in line above.
def add_todo():
    todo_item = request.form.get('add-todo')
    print(todo_item)
    todos_collection = mongo.db.todos
    todos_collection.insert_one({'text' : todo_item, 'complete': False})
    return redirect(url_for('main.index'))