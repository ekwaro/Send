
parcels = [{"product_name": "dan",
            "parcelId":2,
            "userId": 3,
            "weight": 4,
            "price": 4,
            "destination": 4}
            ]
users = []


class User:

    def __init__(self):
        self.user_list = []


class Orders:

    def __init__(self,userId, parceld, product_name, weight, price, destination, current_state):
        self.parcelId = parceld
        self.user_list = userId
        self.product_name = product_name
        self.weight = weight
        self.price = price
        self.current_state = current_state
        self.destination = destination
