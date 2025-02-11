# shops_logic.py

def get_cheapest_prices(shops):
    # Возвращает словарь с минимальными ценами на каждый товар из двух магазинов.
    sweets = {}
    for shop, items in shops.items():
        for item in items:
            name = item['name']
            price = item['price']
            if name not in sweets:
                sweets[name] = []
            sweets[name].append({'shop': shop, 'price': price})

    # Оставляем только два магазина с минимальными ценами для каждого товара
    for sweet, prices in sweets.items():
        sweets[sweet] = sorted(prices, key=lambda x: x['price'])[:2]

    return sweets