from func import people,list,shelf
import unittest

class TestFunction(unittest.TestCase):
    def test_people(self):
        res = people('11-2')
        self.assertEqual(res,"Геннадий Покемонов")
    def test_list(self):
       for doc in documents:
       res_1 = list()    
       self.assertEqual(res_1, print(doc['type'], doc['number'], doc['name']))
    def test_shelf(self):
        res_2 = shelf('10006')
        self.assertEqual(res_2,'2')
