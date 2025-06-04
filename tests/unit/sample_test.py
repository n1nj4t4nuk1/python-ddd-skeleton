import unittest


class TestFindByType(unittest.TestCase):
    def test_sample(self):
        """
        Sample test
        """
        data: int = 39
        data2: int = 39
        self.assertEqual(data, data2)