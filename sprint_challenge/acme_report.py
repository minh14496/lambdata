from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """Use to generate a list of products with a default of 30 products"""
    products = []
    for i in range(num_products):
        prod = Product(
            name=sample(ADJECTIVES, k=1)[0] + ' ' + sample(NOUNS, k=1)[0],
            price=randint(5, 100), weight=randint(5, 100),
            flammability=uniform(0.0, 2.5)
                )
        products.append(prod)

    return products


def inventory_report(products):
    """Print out the reports for the company inventory"""
    s = set()
    price = []
    weight = []
    flammability = []
    for prod in products:
        price.append(prod.price)
        weight.append(prod.weight)
        flammability.append(prod.flammability)
        s.add(prod.name)
    unique = len(s)
    average_price = sum(price)/len(price)
    average_weight = sum(weight)/len(weight)
    average_flammability = sum(flammability)/len(flammability)
    print("```")
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {unique}')
    print(f'Average price: {average_price}')
    print(f'Average weight: {average_weight}')
    print(f'Average flammability: {average_flammability}')
    print("```")


if __name__ == '__main__':
    inventory_report(generate_products())
