import unittest
from operacao import diferenca
from unittest import TestCase


class ModelTest(TestCase):
    def test_diferenca(self):
        self.assertEqual(diferenca(1,3), -1)

if __name__ == '__main__':
    unittest.main()