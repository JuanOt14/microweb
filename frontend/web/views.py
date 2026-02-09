from flask import Flask, render_template
from flask_cors import CORS

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

if __name__ == '__main__':
    app.run()
