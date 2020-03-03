from app import order


def test_order():
    order.add_order_to_db("TEST")
