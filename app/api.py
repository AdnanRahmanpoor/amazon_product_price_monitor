from flask import Blueprint, jsonify
from app.models import Product

app = Blueprint('api', __name__)

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    products_data = [{'name': p.name, 'price': p.price, 'availability': p.availability} for p in products]
    return jsonify(products_data)
