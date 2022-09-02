from func import people,shelf
import unittest

class TestFunction(unittest.TestCase):
    def test_people(self):
        result = people('11-2')
        self.assertEqual(result,"Геннадий Покемонов")
    def test_shelf(self):
        result_2 = shelf('10006')
        self.assertEqual(result_2,'2')
