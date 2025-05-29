from flask import Blueprint
from controllers.users_controller import UsersController

controller = UsersController()
bp_users = Blueprint('users', __name__, url_prefix='/finances/users')

@bp_users.route('', methods=['POST'])
def add():
    return controller.base.add()

@bp_users.route('/all', methods=['GET'])
def get_all():
    return controller.base.get_all()

@bp_users.route('/<int:id>', methods=['GET'])
def get(id):
    return controller.base.get(id)

@bp_users.route('/<int:id>', methods=['PUT'])
def update(id):
    return controller.base.update(id)

@bp_users.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return controller.base.delete(id)