import unittest
from lib.solutions.CHK.checkout_solution import checkout


class MyTestCase(unittest.TestCase):
    def test_product_with_mutiple_offers(self):
        skus = "AAAAAAAA"
        self.assertEqual(checkout(skus), 330)

    def test_product_with_invalid_product_offer(self):
        skus = "AAAEE"
        self.assertEqual(checkout(skus), 210)

    def test_product_with_valid_product_offer(self):
        skus = "AAAEEB"
        self.assertEqual(checkout(skus), 210)

    def test_product_with_multiple_instances(self):
        skus = "AAAAAAAAAA"
        self.assertEqual(checkout(skus), 400)

    def test_valid_offer_placement(self):
        skus = "A" * 15
        self.assertEqual(checkout(skus), 600)

    def test_multiple_product_offers(self):
        skus = "EEEEBB"
        self.assertEqual(checkout(skus), 160)

    def test_multiple_product_offers_2(self):
        skus = "BEBEEE"
        self.assertEqual(checkout(skus), 160)

    def test_best_offer_calcualation(self):
        skus = "ABCDEABCDE"
        self.assertEqual(checkout(skus), 280)

    def test_long_order_1(self):
        skus = "AAAAAEEBAAABB"
        self.assertEqual(checkout(skus), 455)

    def test_long_order_2(self):
        skus = "ABCDECBAABCABBAAAEEAA"
        self.assertEqual(checkout(skus), 665)


if __name__ == '__main__':
    unittest.main()
