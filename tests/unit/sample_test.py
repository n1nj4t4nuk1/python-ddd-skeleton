import unittest


class TestFindByType(unittest.TestCase):
    
    def sample_test(self):
        """
        Sample test
        """
        data: int = 39
        data2: int = 39
        self.assertEqual(data, data2)


if __name__ == '__main__':
    unittest.main()
