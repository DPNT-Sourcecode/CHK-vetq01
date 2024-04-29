import math
from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
# dictionary that has keys as the product names and the values as their prices
# dictionary that has product names as keys and  multi-price offers as the values, ordered by quantity

PRODUCT_COSTS = {}
PRODUCT_MULTI_VALUE_COSTS = defaultdict(list)
PRODUCT_MULTI_VALUE_BOGF = defaultdict(list)
PRODUCT_MULTI_VALUE_COSTS["A"] = [[5, 200], [3, 130]]
PRODUCT_MULTI_VALUE_COSTS["B"] = [[2, 45]]
PRODUCT_MULTI_VALUE_BOGF["E"] = [[2, "B"]]
PRODUCT_MULTI_VALUE_BOGF["F"] = [[3, "F"]]
PRODUCT_MULTI_VALUE_COSTS["H"] = [[10, 80], [5, 45]]
PRODUCT_MULTI_VALUE_COSTS["K"] = [[2, 150]]
PRODUCT_MULTI_VALUE_BOGF["N"] = [[3, "M"]]
PRODUCT_MULTI_VALUE_COSTS["P"] = [[5, 200]]
PRODUCT_MULTI_VALUE_COSTS["Q"] = [[3, 80]]
PRODUCT_MULTI_VALUE_BOGF["R"] = [[3, "Q"]]
PRODUCT_MULTI_VALUE_BOGF["U"] = [[4, "U"]]
PRODUCT_MULTI_VALUE_COSTS["V"] = [[3, 130], [2, 90]]

data_table = """+------+-------+---------------------------------+
| Item | Price | Special offers                  |
+------+-------+---------------------------------+
| A    | 50    | 3A for 130, 5A for 200          |
| B    | 30    | 2B for 45                       |
| C    | 20    |                                 |
| D    | 15    |                                 |
| E    | 40    | 2E get one B free               |
| F    | 10    | 2F get one F free               |
| G    | 20    |                                 |
| H    | 10    | 5H for 45, 10H for 80           |
| I    | 35    |                                 |
| J    | 60    |                                 |
| K    | 70    | 2K for 120                      |
| L    | 90    |                                 |
| M    | 15    |                                 |
| N    | 40    | 3N get one M free               |
| O    | 10    |                                 |
| P    | 50    | 5P for 200                      |
| Q    | 30    | 3Q for 80                       |
| R    | 50    | 3R get one Q free               |
| S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| U    | 40    | 3U get one U free               |
| V    | 50    | 2V for 90, 3V for 130           |
| W    | 20    |                                 |
| X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
+------+-------+---------------------------------+"""

def initialize_costs_and_offers():
    data_file = data_table.split("\n")
    for line in data_file:
        split_line = line.split("|")
        if line[0] == "|" and not ("Item" in split_line[1]):
            PRODUCT_COSTS[split_line[1].strip()] = int(split_line[2].strip())


initialize_costs_and_offers()


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
    for sku in costs_for_each_product:
        quantity = skus_remaining[sku]
        if sku in PRODUCT_MULTI_VALUE_COSTS:
            costs_for_each_product, skus_remaining = get_multi_value_discounts(sku, quantity, costs_for_each_product,
                                                                               sku_frequency, skus_remaining)
    for sku in costs_for_each_product:
        quantity = skus_remaining[sku]
        if sku in PRODUCT_MULTI_VALUE_BOGF:
            costs_for_each_product, skus_remaining = get_multi_value_BOGF(sku, quantity, costs_for_each_product,
                                                                          sku_frequency, skus_remaining)
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
        if not (offer) in skus:
            break
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

