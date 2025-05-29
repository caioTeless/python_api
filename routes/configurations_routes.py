from flask import Blueprint
from controllers.configurations_controller import ConfigurationsController

controller = ConfigurationsController()
bp_configurations = Blueprint('configurations', __name__, url_prefix='/finances/configurations')

@bp_configurations.route('', methods=['POST'])
def add():
    return controller.base.add()

@bp_configurations.route('/all', methods=['GET'])
def get_all():
    return controller.base.get_all()

@bp_configurations.route('/<int:id>', methods=['GET'])
def get(id):
    return controller.base.get(id)

@bp_configurations.route('/<int:id>', methods=['PUT'])
def update(id):
    return controller.base.update(id)

@bp_configurations.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return controller.base.delete(id)