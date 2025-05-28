from flask import request, jsonify
from data.application_db import ApplicationDb

db = ApplicationDb()
db.init_db()

def add_finance():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados inválidos'}), 400
    return db.insert('transactions', data)

def get_all_finances():
    return db.read_all('transactions')

def finances_get(id):
    return db.read_by_id(id)

def update_finance(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados inválidos'}), 400
    data['id'] = id
    return db.update('transactions', data)

def delete_finance(id):
    if id is None:
        return jsonify({'error': 'ID ausente'}), 400
    return db.delete('transactions', id)
