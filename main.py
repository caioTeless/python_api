from flask import Flask
from controllers import transactions_controller as controller

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home page'

@app.route('/finances', methods=['POST'])
def add():
    return controller.add()

@app.route('/finances/all', methods=['GET'])
def get_all():
    return controller.get_all()

@app.route('/finances/<int:id>', methods=['GET'])
def get(id):
    return controller.get(id)

@app.route('/finances/<int:id>', methods=['PUT'])
def update(id):
    return controller.update(id)

@app.route('/finances/<int:id>', methods=['DELETE'])
def delete(id):
    return controller.delete(id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
