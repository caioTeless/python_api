from flask import Blueprint
from controllers.automations_controller import AutomationsController

controller = AutomationsController()
bp_automations = Blueprint('automations', __name__, url_prefix='/finances')

@bp_automations.route('', methods=['POST'])
def add():
    return controller.base.add()

@bp_automations.route('/all', methods=['GET'])
def get_all():
    return controller.base.get_all()

@bp_automations.route('/<int:id>', methods=['GET'])
def get(id):
    return controller.base.get(id)

@bp_automations.route('/<int:id>', methods=['PUT'])
def update(id):
    return controller.base.update(id)

@bp_automations.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return controller.base.delete(id)