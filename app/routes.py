from flask import Blueprint, request, jsonify
from app import db
from app.models import Todo

routes = Blueprint('routes', __name__)

@routes.route('/healthz')
def healthz():
    return jsonify({'status': 'ok', 'version': '1.0'})

@routes.route('/todos',methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([t.to_dict() for t in todos])

@routes.route('/todos/<todo_id>',methods=['GET'])
def get_todo_by_id(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    return jsonify(todo.to_dict()), 200

# POST /todos -> créer une tâche
@routes.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    todo = Todo(title=data["title"])
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo.to_dict()), 201

# PATCH /todos/<todo_id> -> marquer comme fait
@routes.route("/todos/<int:todo_id>", methods=["PATCH"])
def update_todo(todo_id):
 todo = Todo.query.get_or_404(todo_id)
 todo.fait = not todo.fait
 db.session.commit()
 return jsonify(todo.to_dict()), 200

# DELETE /todos/<todo_id> -> supprimer une tâche
@routes.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
 todo = Todo.query.get_or_404(todo_id)
 db.session.delete(todo)
 db.session.commit()
 return jsonify({'message':'TODO DELETED WITH SUCCESS ','status': 'ok'}), 204
