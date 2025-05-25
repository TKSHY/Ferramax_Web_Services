from flask import Blueprint, request, jsonify
from api.services.user_service import UserService
from api.services.product_service import ProductService
from api.services.product_service_by_id import ProductServiceById

def register_routes(app, mysql):
    api_bp = Blueprint('api', __name__)

    user_service = UserService(mysql)
    product_service = ProductService(mysql)
    product_service_by_id = ProductServiceById(mysql)

    @api_bp.route('/users', methods=['GET'])
    def get_users():
        users = user_service.get_all_users()
        return jsonify(users)

    @api_bp.route('/products', methods=['GET'])
    def get_products():
        products = product_service.get_all_products()
        return jsonify(products)
    
    @api_bp.route('/products_by_id', methods=['GET'])
    def get_products_by_id():
        products = product_service_by_id.get_all_products()
    
    # Metodo de pago -


    app.register_blueprint(api_bp)