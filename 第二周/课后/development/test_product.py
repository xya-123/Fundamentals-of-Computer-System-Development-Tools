from product import Product, total


def test_total():
    items = [Product("Keyboard", 199.0), Product("Mouse", 89.0)]
    assert total(items) == 288.0