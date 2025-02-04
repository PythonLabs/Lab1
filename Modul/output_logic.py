# output_logic.py

def print_prices(sweets):
    """
    Выводит цены на сладости в удобном формате.
    """
    for sweet, prices in sweets.items():
        print(f"{sweet}:")
        for price in prices:
            print(f"  {price['shop']}: {price['price']} руб.")