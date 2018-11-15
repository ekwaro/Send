from  flask import jsonify
class Validations:
    @staticmethod
    def validate_input_type(userId,product_name, weight, price, destination):

        if not isinstance(product_name, str):

            return jsonify({'product_name':'product name must be an integer'})
        if not isinstance(userId, int):
            return jsonify({'user_id':'User Id must be an integer'})

        if not isinstance(weight, float):

            return jsonify({'weight':'Weight must have decimal points'})
        if not isinstance(price, float):

            return jsonify({'price':'Price must be a float'})
        if not isinstance(destination, str):

            return jsonify({'destination':'Destination should be a word'})


        if product_name == '':
            return jsonify({'product_name':'product name should be filled'})
        if userId == '':
            return jsonify({'userId':'User Id should be filled'})
        if weight == '':
            return jsonify({'weight':'Weight should be filled'})
        if price == '':
            return jsonify({'price':'price should be filled'})



