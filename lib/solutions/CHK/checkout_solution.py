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
    skus_remaining = create_frequency_dictionary(skus)
    costs_for_each_product = {}
    # Calculate the costs without any offers:
    for sku in sku_frequency:
        quantity = sku_frequency[sku]
        if sku in PRODUCT_COSTS:
            costs_for_each_product[sku] = quantity * PRODUCT_COSTS[sku]
        else:
            return -1
    # Find the best offers to apply to get the lowest cost
    for sku in costs_for_each_product:
        current_cost = costs_for_each_product[sku]
        quantity = sku_frequency[sku]
        if sku in PRODUCT_MULTI_VALUE_COSTS:
            costs_for_each_product,skus_remaining = get_multi_value_costs(sku, quantity, costs_for_each_product, sku_frequency, skus_remaining)
            # Find out the costs for each product, compare to the current cost
            # If better than the current cost, replace, otherwise keep the same
    total_cost = sum(costs_for_each_product.values())
    return total_cost

def get_multi_value_costs(sku, quantity, cost_for_each_product, skus, skus_remaining):
    # iterate through all offers for sku
    cost = 0
    for quantity_threshold, offer in PRODUCT_MULTI_VALUE_COSTS[sku]:
        multi_buy = math.floor(quantity / quantity_threshold)
        # If getting item for free, remove cost accordingly
        if type(offer) == str and offer in skus:
            price_offer = PRODUCT_COSTS[offer]
            multi_buy_offer = math.floor(skus_remaining[sku] / quantity_threshold)
            # Calculate costs of product without any previous offers
            cost_without_offers = (PRODUCT_COSTS[offer] * skus[offer]) - (multi_buy * price_offer)
            # Calculate costs of product with previous offers
            cost_with_offers = cost_for_each_product[offer] - (multi_buy_offer * price_offer)
            # Get the minimum of the above costs
            cost = min(cost_with_offers, cost_without_offers)
            cost_for_each_product[offer] = min(cost, cost_for_each_product[offer])
        # Otherwise discount the price
        elif type(offer) == int:
            cost += multi_buy * offer
            quantity -= multi_buy * quantity_threshold
            skus_remaining[sku] -= multi_buy * quantity_threshold
    # If product remaining, using single buy costs
    if quantity > 0:
        cost += quantity * PRODUCT_COSTS[sku]
    cost_for_each_product[sku] = min(cost, cost_for_each_product[sku])
    return cost_for_each_product, skus_remaining
def create_frequency_dictionary(skus):
    frequency_dictionary = {}
    for sku in skus:
        if sku in frequency_dictionary:
            frequency_dictionary[sku] += 1
        else:
            frequency_dictionary[sku] = 1
    return frequency_dictionary

