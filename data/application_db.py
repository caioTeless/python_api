import os
import sqlite3
from data.schema import TABLE_SCHEMA
from flask import jsonify

class  ApplicationDb:
    def __init__(self):
        base_dir = os.path.abspath(os.path.dirname(__file__))
        self.DATABASE = os.path.join(base_dir, 'finances.db')
    
    def init_db(self):
        try: 
            with sqlite3.connect(self.DATABASE) as conn:
                cursor = conn.cursor()
                for script in TABLE_SCHEMA:
                    cursor.execute(script['query'])  
                conn.commit()
        except sqlite3.Error as e:
            print(f"Erro criando tabela {script['name']}: {e}")

    def get_db_connection(self):
        try: 
            conn = sqlite3.connect(self.DATABASE)
            conn.row_factory = sqlite3.Row
            conn.execute('PRAGMA foreign_keys = ON')
            return conn
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None
        
    def insert(self, table, data):
        if table not in ['transactions', 'users', 'products', 'configurations', 'automations']:
            return jsonify({'error': 'Tabela não permitida'}), 403

        fields = ', '.join(data.keys())
        placeholders = ', ' .join(['?' for _ in data])
        values = list(data.values())
        
        try:
            conn = self.get_db_connection()
            cursor = conn.cursor()
            query = f'INSERT INTO {table} ({fields}) VALUES ({placeholders})'
            cursor.execute(query, values)
            conn.commit()
            conn.close()
            return jsonify({'message': 'Inserido com sucesso'}), 201 
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
    def get_all(self, table):
        try:
            conn = self.get_db_connection()
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {table}')
            objects = [dict(row) for row in cursor.fetchall()]
            conn.close()
            return jsonify(objects)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get(self, table, id):
        try:
            conn = self.get_db_connection()
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {table} WHERE id = {id}')
            row = cursor.fetchone()
            conn.close()
            if row:
                return jsonify(dict(row))
            return jsonify({'error': 'registro não encontrado'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
    def update(self, table, data):
        try:
            record_id = data['id']
            update_data = {key: value for key, value in data.items() if key != 'id'}

            if not update_data:
                return jsonify({'error': 'Nenhum campo para atualizar'}), 400
            
            fields = ', '.join([f"{key}=?" for key in update_data])
            values = list(update_data.values())
            
            values.append(record_id)
            
            conn = self.get_db_connection()
            cursor = conn.cursor()
            query = f'UPDATE {table} SET {fields} WHERE id = ?'
            cursor.execute(query, values)
            conn.commit()
            conn.close()
            
            return jsonify({'message': f'Registro {record_id} atualizado com sucesso'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def delete(self, table, id):
        try:
            conn = self.get_db_connection()
            cursor = conn.cursor()
            cursor.execute(f'DELETE FROM {table} WHERE id = ?', (id))
            conn.commit()
            conn.close()
            return jsonify({'message': f'Registro {id} deletado'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500