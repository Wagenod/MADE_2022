import unittest
from python_advanced.hw01_advanced.hw06 import LRUCache
# from hw06 import LRUCache


class TestLRUCashe(unittest.TestCase):
    lru_cache = LRUCache(3)

    def setUp(self) -> None:
        self.lru_cache.clear()

    def test_just_set(self):
        for i in range(1, 6):
            self.lru_cache['key' + str(i)] = "val" + str(i)
        self.assertListEqual(self.lru_cache.print_cache(), [('key5', 'val5'),
                                                            ('key4', 'val4'),
                                                            ('key3', 'val3')])

    def test_set_single_get_multi(self):
        self.lru_cache['key1'] = "val1"
        for _ in range(5):
            _ = self.lru_cache['key1']
        self.assertListEqual(self.lru_cache.print_cache(), [('key1', 'val1')])

    def test_set_multi_get_multi(self):
        for i in range(1, 6):
            self.lru_cache['key' + str(i)] = "val" + str(i)

        for _ in range(5):
            _ = self.lru_cache['key3']
        self.assertListEqual(self.lru_cache.print_cache(), [('key3', 'val3'),
                                                            ('key5', 'val5'),
                                                            ('key4', 'val4')])

    def test_get(self):
        for i in range(1, 3):
            self.lru_cache['key' + str(i)] = "val" + str(i)

        self.assertIsNone(self.lru_cache['key3'])
        self.assertEqual(self.lru_cache['key1'], 'val1')


if __name__ == "__main__":
    unittest.main()
