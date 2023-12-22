import json

from .settings import DEFAULT_PRICE

def test_product_detail_api(client):
    id = 3
    response = client.get(f"/api/products/{id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert id == data.get('id')
    assert DEFAULT_PRICE * id


def test_product_api(client):
    response = client.get("/api/products")
    print(response.status_code)
    assert response.status_code == 200

def test_post_cart(client):
    
    cart_data = {
        "coupon_code": "NATALSERU20PERSEN",
        "shipping_fee": 4.0,
        "cart_items": [
            {"product_id": 1, "qty": 10},
            {"product_id": 2, "qty": 15}
        ]
    }

    response = client.post("/api/cart", json=cart_data)
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "data created"

def test_get_cart(client):
    cart_id = 1

    response = client.get(f'/api/cart/{cart_id}')

    assert response.status_code == 200

    data = json.loads(response.data)

    assert 'id' in data
    assert 'coupon_code' in data
    assert 'shipping_fee' in data
    assert 'cart_items' in data
    assert 'subtotal' in data
    assert 'grandtotal' in data
    assert 'eligible_promo' in data

    assert data['id'] == cart_id

