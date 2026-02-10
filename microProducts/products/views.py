from flask import Flask
from products.controllers.product_controller import product_controller
from db.db import db
from flask_cors import CORS
from flask_consulate import Consul

app = Flask(__name__)
CORS(app)
app.config.from_object('config.Config')
db.init_app(app)

# Registrar blueprint
app.register_blueprint(product_controller)

# Health check endpoint
@app.route('/healthcheck')
def health_check():
    """
    Health check endpoint for Consul
    Returns 200 if service is healthy
    """
    return '', 200

# Consul registration
consul = Consul(app=app)
consul.register_service(
    name='microproducts',
    interval='10s',
    tags=['products', 'api'],
    port=5003,
    httpcheck='http://localhost:5003/healthcheck'
)

if __name__ == '__main__':
    app.run()
