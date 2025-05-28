from flask import Flask
from controllers import transactions_controller as controller

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home page'

@app.route('/finances', methods=['POST'])
def add_finance():
    return controller.add_finance()

@app.route('/finances/all', methods=['GET'])
def get_all_finances():
    return controller.get_all_finances()

@app.route('/finances/<int:id>', methods=['GET'])
def finances_get(id):
    return controller.finances_get(id)

@app.route('/finances/<int:id>', methods=['PUT'])
def update_finance(id):
    return controller.update_finance(id)

@app.route('/finances/<int:id>', methods=['DELETE'])
def delete_finance(id):
    return controller.delete_finance(id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
