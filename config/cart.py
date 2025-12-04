from django.shortcuts import get_object_or_404
from .models import Producto

def get_cart(session):
    return session.get('cart', {})

def save_cart(session, cart):
    session['cart'] = cart
    session.modified = True


def add_to_cart(session, product_id):
    cart = get_cart(session)
    cart[product_id] = cart.get(product_id, 0) + 1
    save_cart(session, cart)


def remove_from_cart(session, product_id):
    cart = get_cart(session)
    if product_id in cart:
        del cart[product_id]
    save_cart(session, cart)


def clear_cart(session):
    save_cart(session, {})
