def final_price(price, discount=0):
    if price < 0:
        raise ValueError("price must be non-negative")
    if not 0 <= discount <= 1:
        raise ValueError("discount must be between 0 and 1")
    return round(price * (1 - discount), 2)


def get_rate(client):
    return client.get("/rate")["rate"]