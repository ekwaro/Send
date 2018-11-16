
from flask import jsonify, request
from ..models import parcels, Orders
goods = []


class Views:
    @staticmethod
    def get_views(app):
        @app.route('/')
        def homepage():
            return 'Welcome to SendIt', 200

        @app.route('/api/v1/parcels/', methods=['POST'])
        def add_parcel_order():
            order = request.get_json()
            parcelId = len(parcels) + 1
            user_Id = order.get('userId')
            product_name = order.get('product_name')
            weight = order.get('weight')
            price = order.get('price')
            current_state = True
            destination = order.get('destination')

            parcel = Orders(user_Id, parcelId, product_name, weight, price, destination, current_state)
            if parcel.userId == '' or type(parcel.userId) != int:
                return jsonify({'Message': 'User Id cannot be empty and must be a number greater than zero'}), 200
            if parcel.product_name == '' or type(parcel.product_name) is int:
                return jsonify({'Message': 'Product name should be filled and must be a word'}), 200
            if type(parcel.weight) is not float or parcel.weight == '':
                return jsonify({'Message': 'weight must be filled and must be a decimal number'}), 200
            if type(parcel.price) is not float or parcel.price == '':
                return jsonify({"Message": 'Price should be a decimal Number'}), 200
            if type(parcel.destination) == float or parcel.destination.isspace():
                return jsonify({'Message': 'destination should be filled and must be a word'}), 200
            parcel_order = dict(
                        parcelId=parcel.parcelId,
                        userId=parcel.userId,
                        product_name=parcel.product_name,
                        weight=parcel.weight,
                        price=parcel.price,
                        current_state=parcel.current_state,
                        destination=parcel.destination
                            )
            parcels.append(parcel_order)
            return jsonify({
                        'Message':'Added an order successfully',
                        'parcels':parcel_order
                    }), 201


