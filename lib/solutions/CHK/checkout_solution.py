import math
from collections import defaultdict


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Create a dictionary that has keys as the product names and the values as their prices
    product_costs = {"A": 50, "B": 30, "C": 20, "D": 15}
    # Create a dictionary that has product names as keys and  multi-price offers as the values
    product_multi_value_costs = defaultdict(list)
    product_multi_value_costs["A"] = [3, 130]
    product_multi_value_costs["B"] = [2, 45]
    # Create a frequency dictionary of skus given in parameter
    sku_frequency = create_frequency_dictionary(skus)
    total_cost = 0
    for sku in sku_frequency:
        quantity = sku_frequency[sku]
        # If product on offer, check quantity and apply cost accordingly
        if sku in product_multi_value_costs:
            multi_offer_threshold = product_multi_value_costs[sku][0]
            multi_offer_price = product_multi_value_costs[sku][1]
            # Check how many multi-buy offers we have
            multi_buy = math.floor(quantity / multi_offer_threshold)
            # Check product outwith the offer
            single_buy = quantity % multi_offer_threshold
            total_cost = total_cost + (multi_offer_price * multi_buy) + (single_buy * product_costs[sku])
        elif sku in product_costs:
            total_cost += product_costs[sku] * quantity
        # Return -1 in case the product does not exist
        else:
            return -1
    return total_cost

def create_frequency_dictionary(skus):
    frequency_dictionary = {}
    for sku in skus:
        if sku in frequency_dictionary:
            frequency_dictionary[sku] += 1
        else:
            frequency_dictionary[sku] = 1
    return frequency_dictionary

