

# def deco(fn):
#     def inner(*args, **kwargs):
#         print("before", fn.__name__)
#         res = fn(*args, **kwargs)
#         print("after", fn.__name__)
#         return res
#     return inner


# @deco
# def add_nums(a, b):
#     return a + b

# print(add_nums(2, 3))


# def counter(count):
#     while count > 0:
#         yield count
#         count -= 1
#     return 0

# for i in counter(5):
#     print(i)

a = ("abcd"
    "cde")
print(a)


with open("file1.txt", 'w') as file1, open("file2.txt", 'w') as file2:
    print("inside contextmanagers")