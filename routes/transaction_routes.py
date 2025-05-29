from flask import Blueprint
from controllers.transactions_controller import TransactionsController

controller = TransactionsController()
bp_transactions = Blueprint('transactions', __name__, url_prefix='/finances')

@bp_transactions.route('', methods=['POST'])
def add():
    return controller.base.add()

@bp_transactions.route('/all', methods=['GET'])
def get_all():
    return controller.base.get_all()

@bp_transactions.route('/<int:id>', methods=['GET'])
def get(id):
    return controller.base.get(id)

@bp_transactions.route('/<int:id>', methods=['PUT'])
def update(id):
    return controller.base.update(id)

@bp_transactions.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return controller.base.delete(id)