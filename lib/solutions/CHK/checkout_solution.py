import math
from collections import defaultdict


# noinspection PyUnusedLocal
# skus = unicode string
# dictionary that has keys as the product names and the values as their prices
PRODUCT_COSTS = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
# dictionary that has product names as keys and  multi-price offers as the values, ordered by quantity
PRODUCT_MULTI_VALUE_COSTS = defaultdict(list)
PRODUCT_MULTI_VALUE_COSTS["A"] = [[5, 200], [3, 130]]
PRODUCT_MULTI_VALUE_COSTS["B"] = [[2, 45]]
PRODUCT_MULTI_VALUE_COSTS["E"] = [[2, "B"]]
def checkout(skus):
    # Create a frequency dictionary of skus given in parameter
    sku_frequency = create_frequency_dictionary(skus)
    total_cost = 0
    for sku in sku_frequency:
        quantity = sku_frequency[sku]
        # If product on offer, check quantity and apply cost accordingly
        if sku in PRODUCT_MULTI_VALUE_COSTS:
            # get multi-product value of sku
            total_cost = get_multi_value_costs(sku, quantity, total_cost, sku_frequency)
        elif sku in PRODUCT_COSTS:
            total_cost += PRODUCT_COSTS[sku] * quantity
        # Return -1 in case the product does not exist
        else:
            return -1
    return total_cost

def get_multi_value_costs(sku, quantity, total_cost, skus):
    # iterate through all offers for sku
    for quantity_threshold, offer in PRODUCT_MULTI_VALUE_COSTS[sku]:
        multi_buy = math.floor(quantity / quantity_threshold)
        # If getting item for free, remove cost accordingly
        if type(offer) == str and offer in skus:
            offer = PRODUCT_COSTS[offer]
            total_cost -= multi_buy * offer
            quantity -= multi_buy * quantity_threshold
        elif type(offer) == int:
            total_cost += multi_buy * offer
            quantity -= multi_buy * quantity_threshold
    # If product remaining, using single buy costs
    if quantity > 0:
        total_cost += quantity * PRODUCT_COSTS[sku]
    return total_cost
def create_frequency_dictionary(skus):
    frequency_dictionary = {}
    for sku in skus:
        if sku in frequency_dictionary:
            frequency_dictionary[sku] += 1
        else:
            frequency_dictionary[sku] = 1
    return frequency_dictionary

