class LRUCache:

    def __init__(self, limit=42):
        self.limit = limit
        self.cache = {}

    def __getitem__(self, key):
        result = self.cache.pop(key, None)
        if result is not None:
            self.cache[key] = result
        return result

    def __setitem__(self, key, value):
        if key in self.cache:
            del self.cache[key]

        if len(self.cache) == self.limit:
            del self.cache[list(self.cache)[0]]

        self.cache[key] = value


if __name__ == "__main__":
    cache = LRUCache(3)

    cache['k1'] = "val1"
    cache['k2'] = "val2"

    print(cache["k3"])  # None
    print(cache["k2"])  # "val2"
    print(cache["k1"])  # "val1"

    cache["k3"] = "val3"

    print(cache["k3"])  # "val3"
    print(cache["k2"])  # None
    print(cache["k1"])  # "val1"
