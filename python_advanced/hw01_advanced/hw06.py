from collections import deque
import logging
import logging.config

import logger_config

logging.config.dictConfig(logger_config.LOG_CONFIG)
logger = logging.getLogger("main")

class LRUCache:

    def __init__(self, logger=None, limit=42):
        self.logger = logger
        self.limit = limit
        self.init_cache()

    def init_cache(self):
        self.logger.info("Initialize LRU-cache with limit size %s", self.limit)
        self.key_idx_mapping = {}
        self.value_storage = deque()

    def _add_new_pair(self, key, value):
        self.value_storage.append(value)
        self.key_idx_mapping[key] = len(self.value_storage) - 1

    def _update_lru_cashe(self, key, value=None):
        idx = self.key_idx_mapping[key]
        new_value = self.value_storage[idx] if value is None else value
        del self.value_storage[idx]
        for k, i in self.key_idx_mapping.items():
            self.key_idx_mapping[k] = i - 1 if i > idx else i
        self._add_new_pair(key, new_value)

    def __getitem__(self, key):  # O(n)
        self.logger.info("Getting item with key %s", key)
        if key not in self.key_idx_mapping:
            self.logger.warning("Item with key %s not exist", key)
            return None
        value = self.value_storage[self.key_idx_mapping[key]]
        self.logger.info("Got value = {}".format(value))
        self._update_lru_cashe(key)  # O(n)
        self.logger.debug("LRU-cashe before state update {} {}".format(self.key_idx_mapping, self.value_storage))
        return value

    def __setitem__(self, key, value):  # O(n)
        self.logger.info("Add new pair ({},{}) to LRU-cache".format(key, value))
        if key in self.key_idx_mapping:
            self._update_lru_cashe(key, value)
        else:
            if len(self.value_storage) == self.limit:
                self.logger.warning("LRU-cache is full!!")
                self.value_storage.popleft()
                self.key_idx_mapping = {k: v - 1 for k, v in self.key_idx_mapping.items() if v}
            self._add_new_pair(key, value)
        self.logger.debug("LRU-cashe before state update {} {}".format(self.key_idx_mapping, self.value_storage))

    def print_cache(self):  # O(n)
        merged = [None]*len(self.key_idx_mapping)
        for k, i in self.key_idx_mapping.items():
            merged[- i - 1] = (k, self.value_storage[i])
        return merged


if __name__ == "__main__":
    cache = LRUCache(logger=logger, limit=3)
    cache['k1'] = "val1"
    cache['k2'] = "val2"
    print(cache["k3"])  # None
    print(cache["k2"])  # "val2"
    print(cache["k1"])  # "val1"
    cache["k3"] = "val3"
    print(cache["k3"])  # "val3"
    print(cache["k2"])  # None
    print(cache["k1"])  # "val1"
