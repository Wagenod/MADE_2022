from collections import deque

class LRUCache:

    def __init__(self, limit=42):
        self.limit = limit
        self.key_idx_storage = {}
        self.value_storage = deque()

    def add_to_storages(self, key, value):
        self.value_storage.append(value)
        self.key_idx_storage[key] = len(self.value_storage) - 1


    def _update_lru_cashe(self, key, value=None):
        idx = self.key_idx_storage[key]
        new_value = self.value_storage[idx] if value is None else value

        del self.value_storage[idx]
        for k, i in self.key_idx_storage.items():
            self.key_idx_storage[k] = i - 1 if i > idx else i

        self.add_to_storages(key, new_value)

    def __getitem__(self, key):
        if key not in self.key_idx_storage:
            return None
        value = self.value_storage[self.key_idx_storage[key]]
        self._update_lru_cashe(key)
        return value


    def __setitem__(self, key, value):
        if key in self.key_idx_storage:
            self._update_lru_cashe(key, value)
        else:
            if len(self.value_storage) == self.limit:
                self.value_storage.popleft()
                self.key_idx_storage = {k: v -1 for k, v in self.key_idx_storage.items() if v}
                
                self.add_to_storages(key, value)
            else:
                self.add_to_storages(key, value)

    def merge_storages(self):
        merged = [None]*len(self.key_idx_storage)
        for k, i in self.key_idx_storage.items():
            merged[i] = (k, self.value_storage[i])
        return merged
        


if __name__ == "__main__":
    cache = LRUCache(3)

    cache['k1'] = "val1"
    print(cache.key_idx_storage, cache.value_storage)
    cache['k2'] = "val2"
    print(cache.key_idx_storage, cache.value_storage)

    print(cache["k3"])  # None
    print(cache.key_idx_storage, cache.value_storage)

    print(cache["k2"])  # "val2"
    print(cache.key_idx_storage, cache.value_storage)

    print(cache["k1"])  # "val1"
    print(cache.key_idx_storage, cache.value_storage)

    cache["k3"] = "val3"
    print(cache.key_idx_storage, cache.value_storage)

    print(cache["k3"])  # "val3"
    print(cache.key_idx_storage, cache.value_storage)

    print(cache["k2"])  # None
    print(cache.key_idx_storage, cache.value_storage)

    print(cache["k1"])  # "val1"
    print(cache.key_idx_storage, cache.value_storage)
    print(cache.merge_storages())
