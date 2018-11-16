import pytest
import json
import manage

class TestCases:
    @pytest.fixture
    def client(self):
        test_client = manage.server().test_client()
        return test_client

    def test_home_page(self, client):
        response = client.get('/')
        assert response.status_code == 200
        assert b"Welcome to SendIt" in response.data

    def test_get_all_parcels(self, client):
        response = client.get('/api/v1/parcels/')
        assert response.status_code == 200
        assert b"Your parcels are here" in response.data
        assert b"parcels" in response.data

    def test_get_order_by_id(self, client):
        response = client.get('/api/v1/parcels/2')
        assert response.status_code == 200
        assert b"Here is the parcel you requested for" in response.data

    def test_certain_parcel_id_not_found(self, client):
        response = client.get('api/v2/parcels/8')
        assert response.status_code == 404

    def test_post1_order(self, client):
        response = client.post('/api/v1/parcels/', content_type='application/json', data=json.dumps({
            "destination": "Kamwokya",
            "parcelId": 2,
            "price": 4.0,
            "product_name": "dan",
            "userId": 3,
            "weight": 4.0
            }))
        assert response.status_code == 201
        assert b"Added an order successfully" in response.data
        assert b"weight" in response.data


    def test_cancel_parcel(self, client):
        response = client.put('/api/v1/parcels/2/cancel/')
        assert b"current_state = False"
        assert b"parcel cancelled" in response.data
        assert response.status_code == 200

    def test_parcel_order_not_cancelled(self, client):
        response = client.put('/api/V1/parcels/2/cancel/')
        assert response.status_code == 404

    def test_get_specific_user_parcels(self, client):
        response = client.get('/api/v1/users/3/parcels/')
        assert response.status_code == 200
        assert b"All parcel order created is displayed below"

    def test_user_parcel_doesnot_exists(self, client):
        response = client.get('/api/v1/users/5/parcels/')
        assert response.status_code == 404


