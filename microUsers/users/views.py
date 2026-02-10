from flask import Flask, render_template
from users.controllers.user_controller import user_controller
from db.db import db
from flask_cors import CORS
from flask_consulate import Consul

app = Flask(__name__)
CORS(app)
app.config.from_object('config.Config')
db.init_app(app)

# Registrando el blueprint del controlador de usuarios
app.register_blueprint(user_controller)

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
    name='microusers',
    interval='10s',
    tags=['users', 'api'],
    port=5002,
    httpcheck='http://localhost:5002/healthcheck'
)

if __name__ == '__main__':
    app.run()
