import unittest
from hw06 import LRUCache


class TestLRUCashe(unittest.TestCase):
    lru_cache = LRUCache(3)

    def test_just_set(self):
        self.lru_cache.cache = {}
        self.lru_cache['key1'] = "val1"
        self.lru_cache['key2'] = "val2"
        self.lru_cache['key3'] = "val3"
        self.lru_cache['key4'] = "val4"
        self.lru_cache['key5'] = "val5"
        self.assertDictEqual(self.lru_cache.cache, {'key5': 'val5', 'key4': 'val4', 'key3': 'val3'})

    def test_set_single_get_multi(self):
        self.lru_cache.cache = {}
        self.lru_cache['key1'] = "val1"
        for _ in range(5):
            r = self.lru_cache['key1']
        self.assertDictEqual(self.lru_cache.cache, {'key1': 'val1'})

    def test_set_multi_get_multi(self):
        self.lru_cache.cache = {}
        self.lru_cache['key1'] = "val1"
        self.lru_cache['key2'] = "val2"
        self.lru_cache['key3'] = "val3"
        self.lru_cache['key4'] = "val4"
        self.lru_cache['key5'] = "val5"
        for _ in range(5):
            r = self.lru_cache['key3']
        self.assertDictEqual(self.lru_cache.cache, {'key3': 'val3', 'key5': 'val5', 'key4': 'val4'})

    def test_get(self):
        self.lru_cache.cache = {}
        self.lru_cache['key1'] = "val1"
        self.lru_cache['key2'] = "val2"

        self.assertIsNone(self.lru_cache['key3'])
        self.assertEqual(self.lru_cache['key1'], 'val1')


if __name__ == "__main__":
    unittest.main()
