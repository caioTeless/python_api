from flask import Flask
from routes.transaction_routes import bp_transactions
from routes.products_routes import bp_products
from routes.users_routes import bp_users
from routes.configurations_routes import bp_configurations
from routes.automations_routes import bp_automations

app = Flask(__name__)

app.register_blueprint(bp_transactions)
app.register_blueprint(bp_products)
app.register_blueprint(bp_users)
app.register_blueprint(bp_configurations)
app.register_blueprint(bp_automations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
