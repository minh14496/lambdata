import pytest
from acme import BoxingGlove, Product
from acme_report import generate_products, ADJECTIVES, NOUNS


def test_default_product_price():
    """Test default product price being 10."""
    prod = Product('Test Product')
    assert prod.price == 10


def test_stealability():
    """Test stealability from acme"""
    prod = Product('Test Product', price=10, weight=10)
    assert prod.stealability() == 'Very stealable!'
    prod = Product('Test Product', price=10, weight=30)
    assert prod.stealability() == 'Not so stealable...'
    prod = Product('Test Product', price=10, weight=20)
    assert prod.stealability() == 'Kinda stealable.'


def test_explode():
    """Test explode function from acme"""
    prod = Product('Test Product', weight=10, flammability=0.5)
    assert prod.explode() == '...fizzle.'
    prod = Product('Test Product', weight=20, flammability=2)
    assert prod.explode() == '...boom!'
    prod = Product('Test Product', weight=30, flammability=2.5)
    assert prod.explode() == '...BABOOM!!'


def test_default_num_products():
    """
    Test the default number of products generate by
    generate_products function from acme_test
    """
    products = generate_products()
    assert len(products) == 30


def test_legal_names():
    """
    test_legal_names Test if the products name are valid possible names
    to genertate(adjecive, space, noun) from the list of possible words
    """
    products = generate_products()
    for prod in products:
        assert prod.name.split(' ')[0] in ADJECTIVES
        assert prod.name.split(' ')[1] in NOUNS


def test_inventory_report():
    # TODO create a test for inventory report
    pass
