from flask import request, jsonify
from data.application_db import ApplicationDb

class BaseController():
    def __init__(self, table):
        self.db = ApplicationDb()
        self.db.init_db()
        self.table = table
        
    def add(self):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Dados inválidos'}), 400
        return self.db.insert(self.table, data)

    def get_all(self):
        return self.db.get_all(self.table)

    def get(self, id):
        return self.db.get(self.table, id)

    def update(self, id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Dados inválidos'}), 400
        data['id'] = id
        return self.db.update(self.table, data)

    def delete(self, id):
        if id is None:
            return jsonify({'error': 'ID ausente'}), 400
        return self.db.delete(self.table, id)
