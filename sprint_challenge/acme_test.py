import pytest
from acme import Product, BoxingGlove
from acme_report import generate_products, ADJECTIVES, NOUNS, inventory_report


@pytest.fixture
def new_product():
    """Create Product with different parameter value"""
    return Product(name='Test Product', price=20, weight=30, flammability=2)


@pytest.fixture
def products():
    """Generate a bunch of product with default value"""
    return generate_products()


def test_default_product_price():
    """Test default product price being 10."""
    prod = Product('Test Product')
    assert prod.price == 10


def test_stealability(new_product):
    """Test stealability from acme"""
    assert new_product.stealability() == 'Kinda stealable.'


def test_explode(new_product):
    """Test explode function from acme"""
    assert new_product.explode() == '...BABOOM!!'


def test_punch():
    """"Test punch function from acme"""
    glove = BoxingGlove('Glove', weight=15)
    assert glove.punch() == 'OUCH!'


def test_default_num_products(products):
    """
    Test the default number of products generate by
    generate_products function from acme_test
    """
    assert len(products) == 30


def test_legal_names(products):
    """
    test_legal_names Test if the products name are valid possible names
    to genertate(adjecive, space, noun) from the list of possible words
    """
    for prod in products:
        assert prod.name.split(' ')[0] in ADJECTIVES
        assert prod.name.split(' ')[1] in NOUNS


def test_inventory_report(capfd, products):
    names = set()
    total_price = 0
    total_weight = 0
    total_flammability = 0.0
    for product in products:
        names.add(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability

    avg_price = total_price / len(products)
    avg_weight = total_weight / len(products)
    avg_flammability = total_flammability / len(products)
    inventory_report(products)
    out, err = capfd.readouterr()
    assert str(len(names)) in out
    assert str(avg_price) in out
    assert str(avg_weight) in out
    assert str(avg_flammability) in out
