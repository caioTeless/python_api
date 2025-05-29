from flask import Blueprint
from controllers.products_controller import ProductsController

controller = ProductsController()
bp_products = Blueprint('products', __name__, url_prefix='/finances/products')

@bp_products.route('', methods=['POST'])
def add():
    return controller.base.add()

@bp_products.route('/all', methods=['GET'])
def get_all():
    return controller.base.get_all()

@bp_products.route('/<int:id>', methods=['GET'])
def get(id):
    return controller.base.get(id)

@bp_products.route('/<int:id>', methods=['PUT'])
def update(id):
    return controller.base.update(id)

@bp_products.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return controller.base.delete(id)