
from flask import jsonify, request
from ..models import parcels, Orders
from .errors import Validations
goods = []


class Views:
    @staticmethod
    def get_views(app):


        @app.route('/api/v1/parcels/', methods=['GET'])
        def get_parcels():
            return jsonify({
                "message": "Your parcels are here",
                "parcels": parcels
            }), 200

