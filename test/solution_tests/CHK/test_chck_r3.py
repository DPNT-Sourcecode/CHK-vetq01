import unittest
from lib.solutions.CHK.checkout_solution import checkout

class MyTestCase(unittest.TestCase):

    def test_reworded_offer(self):
        skus = "FF"
        self.assertEqual(checkout(skus), 20)

    def test_reworded_offer_with_other_offers(self):
        skus = "FFBBEE"
        self.assertEqual(checkout(skus), 130)

    def test_multiple_reworded_offer(self):
        skus = "FFFFFF"
        self.assertEqual(checkout(skus), 40)

    def test_reworded_offer_with_additional_item(self):
        skus = "FFFBBEE"
        self.assertEqual(checkout(skus), 120)


if __name__ == '__main__':
    unittest.main()



