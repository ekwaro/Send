
parcels = [{
    "destination": 4,
    "parcelId": 2,
    "price": 4,
    "product_name": "dan",
    "userId": 3,
    "weight": 4
             }
]


class Orders:

    def __init__(self,userId, parceId, product_name, weight, price, destination, current_state):
        self.parcelId = parceId
        self.userId = userId
        self.product_name = product_name
        self.weight = weight
        self.price = price
        self.current_state = current_state
        self.destination = destination
