from flask import Blueprint, request, jsonify
from app.extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.product import Product

product_bp = Blueprint("product", __name__)

products = []

@product_bp.route("/", methods=["POST"])
@jwt_required()
def create_product():
    data = request.json

    user_id = get_jwt_identity()

    product = Product(
        name=data["name"],
        user_id=user_id
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({"msg": "Producto creado"})

@product_bp.route("/", methods=["GET"])
@jwt_required()
def get_products():
    user_id = get_jwt_identity()

    products = Product.query.filter_by(user_id=user_id).all()

    result = []
    for p in products:
        result.append({
            "id": p.id,
            "name": p.name
        })

    return jsonify(result)