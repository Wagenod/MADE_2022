from itertools import zip_longest


class CustomList(list):
    def __init__(self, items):
        super().__init__()
        if not isinstance(items, (list, tuple)):
            raise TypeError("Argument must be list or tuple")

        self.__idx = -1
        self.items = list(items)

    def __sub__(self, another):
        return CustomList([x - y for x, y in zip_longest(self, another, fillvalue=0)])

    def __rsub__(self, another):
        return CustomList([y - x for x, y in zip_longest(self, another, fillvalue=0)])

    def __add__(self, another):
        return CustomList([x + y for x, y in zip_longest(self, another, fillvalue=0)])

    def __radd__(self, another):
        return self.__add__(another)
    
    def __iter__(self):
        return self

    def __next__(self):
        self.__idx += 1
        if self.__idx >= len(self.items):
            self.__idx = -1
            raise StopIteration
        
        return self.items[self.__idx]

    def __repr__(self):
        return f"CustomList({self.items})"

    def __str__(self):
        return f"CustomList items: {self.items} sum= {sum(self.items)}"

    def __eq__(self, another) -> bool:
        return sum(self.items) == sum(another.items)

    def __ne__(self, another) -> bool:
        return sum(self.items) != sum(another.items)

    def __le__(self, another) -> bool:
        return sum(self.items) <= sum(another.items)

    def __ge__(self, another) -> bool:
        return sum(self.items) >= sum(another.items)

    def __lt__(self, another) -> bool:
        return sum(self.items) < sum(another.items)

    def __gt__(self, another) -> bool:
        return sum(self.items) > sum(another.items)


# -
assert repr((CustomList([1, 3, 6]) - CustomList([0, 4]))) == repr(CustomList([1, -1, 6]))
assert repr(([5, 0, 6] - CustomList([2, 1]))) == repr(CustomList([3, -1, 6]))
assert repr((CustomList([2, 1]) - [5, 0, 6])) == repr(CustomList([-3, 1, -6]))
assert repr((CustomList([2, 1]) - [])) == repr(CustomList([2, 1]))
assert repr((CustomList([]) - [])) == repr(CustomList([]))
assert repr((CustomList([]) - [2, 1])) == repr(CustomList([-2, -1]))

# +
assert repr((CustomList([1, 3, 6]) + CustomList([0, 4]))) == repr(CustomList([1, 7, 6]))
assert repr([5, 0, 6] + CustomList([2, 1])) == repr(CustomList([7, 1, 6]))
assert repr((CustomList([2, 1]) + [5, 0, 6])) == repr(CustomList([7, 1, 6]))
assert repr((CustomList([]) + [])) == repr(CustomList([]))
assert repr((CustomList([]) + [2, 1])) == repr(CustomList([2, 1]))

# ==

assert CustomList([2, 1, 4]) == CustomList([7])
assert CustomList([2, 1, 4, 5]) != CustomList([7])
assert CustomList([2, 1, 4, 5]) > CustomList([7])
assert CustomList([2, 1, 4, 5]) < CustomList([7, 10])
assert CustomList([2, 1]) <= CustomList([3])
assert CustomList([2, 1]) >= CustomList([3])
assert CustomList([]) == CustomList([])
assert CustomList((2,)) == CustomList([1, 1])

# __str__
assert str(CustomList([12, 34, 5.2])) == "CustomList items: [12, 34, 5.2] sum= 51.2"
print(CustomList({"123", 34, 5.2}))
