
from flask import jsonify, request
from ..models import parcels, Orders
from .errors import Validations
goods = []


class Views:

    @staticmethod
    def get_views(app):

        # @app.route('/')
        # def homepage():
        #     return 'Welcome to SendIt', 200
        #
        # @app.route('/api/v1/parcels/', methods=['GET'])
        # def get_parcels():
        #     return jsonify({
        #         "message": "Your parcels are here",
        #         "parcels": parcels
        #     }), 200
        #
        # @app.route('/api/v1/parcels/<int:parcelId>', methods=['GET'])
        # def get_parcel_by_id(parcelId):
        #     for parcel in parcels:
        #         if parcel['parcelId'] == parcelId:
        #             return jsonify({
        #                 "Message": "Here is the parcel you requested for",
        #                 "parcel": parcel
        #             }), 200
        #
        # @app.route('/api/v1/parcels/<int:parcelId>/cancel/', methods=['PUT'])
        # def edit_parcels(parcelId):
        #     for parcel in parcels:
        #         if parcel['parcelId'] == parcelId:
        #             parcel['current_state'] = False
        #             return jsonify({
        #                     'Message': 'parcel cancelled',
        #                     'parcel': parcel
        #             })

        @app.route('/api/v1/parcels/', methods=['POST'])
        def add_parcel_order():
            order = request.get_json()
            parcelId = len(parcels) + 1
            user_Id = order.get('user_list')
            product_name = order.get('product_name')
            weight = order.get('weight')
            price = order.get('price')
            current_state = True
            destination = order.get('destination')
            if Validations.validate_input_type(user_Id, product_name, weight, price, destination):
                parcel = Orders(user_Id, parcelId, product_name, weight, price, destination, current_state)
                parcel_order = dict(
                        parcelId=parcel.parcelId,
                        user_list=parcel.user_list,
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


        # @app.route('/api/v1/users/<int:userIdt>/parcels/', methods=['GET'])
        # def get_all_orders_for_particular_user(userId):
        #     user_parcels = []
        #     for person in parcels:
        #         if person['user_list'] == userId:
        #             user_parcels.append(person)
        #
        #     if len(user_parcels) > 0:
        #         return jsonify({"Message":"All parcel order created is displayed below",
        #                         "user_data": user_parcels})
        #     return jsonify({"user_parcels": "user does not exist"})









