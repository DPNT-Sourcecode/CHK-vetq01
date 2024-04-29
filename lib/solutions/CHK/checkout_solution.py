import math
from collections import defaultdict


# noinspection PyUnusedLocal
# skus = unicode string
# dictionary that has keys as the product names and the values as their prices
PRODUCT_COSTS = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
# dictionary that has product names as keys and  multi-price offers as the values, ordered by quantity
PRODUCT_MULTI_VALUE_COSTS = defaultdict(list)
PRODUCT_MULTI_VALUE_BOGF = defaultdict(list)
PRODUCT_MULTI_VALUE_COSTS["A"] = [[5, 200], [3, 130]]
PRODUCT_MULTI_VALUE_COSTS["B"] = [[2, 45]]
PRODUCT_MULTI_VALUE_BOGF["E"] = [[2, "B"]]
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
        quantity = skus_remaining[sku]
        if sku in PRODUCT_MULTI_VALUE_COSTS:
            costs_for_each_product,skus_remaining = get_multi_value_discounts(sku, quantity, costs_for_each_product, sku_frequency, skus_remaining)
    for sku in costs_for_each_product:
        quantity = skus_remaining[sku]
        if sku in PRODUCT_MULTI_VALUE_BOGF:
            costs_for_each_product,skus_remaining = get_multi_value_BOGF(sku, quantity, costs_for_each_product, sku_frequency, skus_remaining)
    total_cost = sum(costs_for_each_product.values())
    return total_cost

def get_multi_value_discounts(sku, quantity, cost_for_each_product, skus, skus_remaining):
    cost = 0
    for quantity_threshold, offer in PRODUCT_MULTI_VALUE_COSTS[sku]:
        multi_buy = math.floor(quantity / quantity_threshold)
        # If getting item for free, remove cost accordingly
        cost += multi_buy * offer
        quantity -= multi_buy * quantity_threshold
        skus_remaining[sku] -= multi_buy * quantity_threshold
    if quantity > 0:
        cost += quantity * PRODUCT_COSTS[sku]
    cost_for_each_product[sku] = min(cost, cost_for_each_product[sku])
    return cost_for_each_product, skus_remaining


def get_multi_value_BOGF(sku, quantity, cost_for_each_product, skus, skus_remaining):
    # iterate through all offers for sku
    cost = 0
    for quantity_threshold, offer in PRODUCT_MULTI_VALUE_BOGF[sku]:
        multi_buy = math.floor(quantity / quantity_threshold)
        price_offer = PRODUCT_COSTS[offer]
        # Calculate costs of product without any previous offers
        cost_without_offers = price_offer * skus[offer]
        cost_with_offers = cost_for_each_product[offer]
        for i in range(0, multi_buy):
            if cost_without_offers == 0:
                break
            cost_without_offers -= price_offer
        skus_left_offer = skus_remaining[offer]
        for i in range(0, multi_buy):
            if cost_with_offers == 0 or skus_left_offer == 0:
                break
            cost_with_offers -= price_offer
            skus_left_offer -= 1
        # Calculate costs of product with previous offers
        cost = min(cost_without_offers, cost_with_offers)
        cost_for_each_product[offer] = min(cost, cost_for_each_product[offer])
        # Otherwise discount the price
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




