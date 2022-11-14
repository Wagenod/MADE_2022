from collections import deque


class LRUCache:

    def __init__(self, limit=42):
        self.limit = limit
        self.clear()

    def clear(self):
        self.key_idx_storage = {}
        self.value_storage = deque()

    def _add_new_pair(self, key, value):
        self.value_storage.append(value)
        self.key_idx_storage[key] = len(self.value_storage) - 1

    def _update_lru_cashe(self, key, value=None):
        idx = self.key_idx_storage[key]
        new_value = self.value_storage[idx] if value is None else value
        del self.value_storage[idx]
        for k, i in self.key_idx_storage.items():
            self.key_idx_storage[k] = i - 1 if i > idx else i
        self._add_new_pair(key, new_value)

    def __getitem__(self, key):  # O(n)
        if key not in self.key_idx_storage:
            return None
        value = self.value_storage[self.key_idx_storage[key]]
        self._update_lru_cashe(key)  # O(n)
        return value

    def __setitem__(self, key, value):  # O(n)
        if key in self.key_idx_storage:
            self._update_lru_cashe(key, value)
        else:
            if len(self.value_storage) == self.limit:
                self.value_storage.popleft()
                self.key_idx_storage = {k: v - 1 for k, v in self.key_idx_storage.items() if v}
            self._add_new_pair(key, value)

    def print_cache(self):  # O(n)
        merged = [None]*len(self.key_idx_storage)
        for k, i in self.key_idx_storage.items():
            merged[- i - 1] = (k, self.value_storage[i])
        return merged


if __name__ == "__main__":
    cache = LRUCache(3)
    cache['k1'] = "val1"
    print(cache.key_idx_storage, cache.value_storage, cache.print_cache())
    cache['k2'] = "val2"
    print(cache.key_idx_storage, cache.value_storage, cache.print_cache())
    print(cache["k3"])  # None
    print(cache["k2"])  # "val2"
    print(cache["k1"])  # "val1"
    cache["k3"] = "val3"
    print(cache.key_idx_storage, cache.value_storage, cache.print_cache())
    print(cache["k3"])  # "val3"
    print(cache["k2"])  # None
    print(cache["k1"])  # "val1"
    print(cache.key_idx_storage, cache.value_storage, cache.print_cache())
