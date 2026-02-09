from flask import Blueprint, request, jsonify
from products.models.product_model import Products
from db.db import db

product_controller = Blueprint('product_controller', __name__)

# GET all
@product_controller.route('/api/products', methods=['GET'])
def get_products():
    products = Products.query.all()
    result = [
        {
            'id': p.id,
            'name': p.name,
            'description': p.description,
            'price': float(p.price),
            'stock': p.stock
        } for p in products
    ]
    return jsonify(result)

# GET one by id
@product_controller.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    p = Products.query.get_or_404(product_id)
    return jsonify({
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'price': float(p.price),
        'stock': p.stock
    })

# POST create
@product_controller.route('/api/products', methods=['POST'])
def create_product():
    data = request.json

    new_product = Products(
        name=data['name'],
        description=data.get('description', ''),
        price=data.get('price', 0),
        stock=data.get('stock', 0)
    )

    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message': 'Product created successfully'}), 201

# PUT update
@product_controller.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    p = Products.query.get_or_404(product_id)
    data = request.json

    p.name = data['name']
    p.description = data.get('description', '')
    p.price = data.get('price', 0)
    p.stock = data.get('stock', 0)

    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

# DELETE
@product_controller.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    p = Products.query.get_or_404(product_id)
    db.session.delete(p)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})
