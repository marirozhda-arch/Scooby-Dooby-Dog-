from product import Product
from datetime import date
from console_helper import *

global_product_id = 0

def get_next_product_id() -> int:
    global global_product_id

    global_product_id += 1

    return global_product_id

def input_product_data() -> Product:
    icon = input_str()
    best_before_date = input_date()
    
    name = input_str()
    category = input_str()
    price = input_int()
    rating = input_float()

    return Product(
        icon=icon,
        best_before_date=best_before_date,
        name=name,
        category=category,
        price=price,
        rating=rating,
    )

def get_product_by_id(products: list[Product], search_id: int) -> Product | None:
    for product in products:
        if product.id == search_id:
            return product

    return None


def add_product_to_list(products: list[Product], product: Product):
    products.append(product)

def update_product_by_id(products: list[Product], product: Product) -> bool:
    find_product = get_product_by_id(products, product.id)

    if find_product == None:
        return False

    find_product.icon = product.icon
    find_product.best_before_date = product.best_before_date
    find_product.name = product.name
    find_product.category = product.category
    find_product.price = product.price
    find_product.rating = product.rating
    

    return True
