from api import create_folder
import unittest


class TestFunction(unittest.TestCase):
    def test_test_api(self):
      folder_name = 'test_api_ya'
      result = create_folder(folder_name)
      self.assertTrue(result == 409, f'Сервер ответил: {result}')
