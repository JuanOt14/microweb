from flask import Flask, render_template
from flask_cors import CORS
from flask_consulate import Consul

app = Flask(__name__)
CORS(app)
app.config.from_object('config.Config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/editUser/<string:id>')
def edit_user(id):
    return render_template('editUser.html', id=id)

# ✅ NUEVO: products
@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/editProduct/<string:id>')
def edit_product(id):
    return render_template('editProduct.html', id=id)

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
    name='frontend',
    interval='10s',
    tags=['web', 'frontend'],
    port=5001,
    httpcheck='http://localhost:5001/healthcheck'
)

if __name__ == '__main__':
    app.run()
