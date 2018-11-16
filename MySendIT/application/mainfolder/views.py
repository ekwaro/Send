
from flask import jsonify, request
from ..models import parcels, Orders
goods = []


class Views:
    @staticmethod
    def get_views(app):
        @app.route('/')
        def homepage():
            return 'Welcome to SendIt', 200

        @app.route('/api/v1/parcels/', methods=['GET'])
        def get_parcels():
            if len(parcels) >0:
                return jsonify({
                 "message": "Your parcels are here",
                 "parcels": parcels
            }), 200
            else:
                return jsonify({'Message':'Parcels are not yet created'})

        @app.route('/api/v1/parcels/<int:parcelId>', methods=['GET'])
        def get_parcel_by_id(parcelId):
            for parcel in parcels:
                if parcel['parcelId'] == parcelId:
                    return jsonify({
                        "Message": "Here is the parcel you requested for",
                        "parcel": parcel
                    }), 200
                else:
                    return jsonify({'Message': 'parcel Id not found'}), 404

        @app.route('/api/v1/parcels/<int:parcelId>/cancel/', methods=['PUT'])
        def edit_parcels(parcelId):
            for parcel in parcels:
                if parcel['parcelId'] == parcelId:
                    parcel['current_state'] = False
                    return jsonify({
                            'Message': 'parcel cancelled',
                            'parcel': parcel
                    }), 200
                else:
                    return jsonify({'Message':'Item with the given Id does not exist'}), 404

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

        @app.route('/api/v1/users/<int:userId>/parcels/', methods=['GET'])
        def get_all_orders_for_particular_user(userId):
            user_parcels = []
            for person in parcels:
                if person['userId'] == userId:
                    user_parcels.append(person)

            if len(user_parcels) > 0:
                return jsonify({"Message":"All parcel order created is displayed below",
                                "user_data": user_parcels}), 200

            else:
                return jsonify({"user_parcels": "user does not exist"}), 404

