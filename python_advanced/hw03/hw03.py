import json
import time
import random

# 1. Написать функцию, которая в качестве аргументов принимает строку json,
# список полей, которые необходимо обработать, список имён, которые нужно
# найти и функцию-обработчика имени, который срабатывает, когда в каком-либо
# поле было найдено ключевое имя.

# Функция, должна принимать строку, в которой содержится json, и произвести
# парсинг этого json. Упростим немного и представим, что json представляет
# из себя только коллекцию ключей-значений. Причём ключами и значениями
# являются только строки.

''' def parse_json(json_str: str,
                    required_fields=None,
                    keywords=None,
                    keyword_callback)

    Например, представим, что
            json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
            required_fields = ["key1"]
            keywords = ["word2"]
    Тогда keyword_callback будет вызвана только для слова word2 для ключа key1.
'''


stats = {}


def stats_counter(word):
    if word not in stats:
        stats[word] = 1
    else:
        stats[word] += 1


def parse_json(json_str: str, keyword_callback,
               required_fields=None, keywords=None):
    if not json_str or required_fields is None or keywords is None:
        raise ValueError("Arguments json_str, required_fields, keywords \
                        must take some value, not None or empty value")

    if not callable(keyword_callback):
        raise TypeError("Argument keyword_callback must be callable")

    json_dict = json.loads(json_str)

    for kw in keywords:
        for field in required_fields:
            if kw in json_dict[field].split(" "):
                keyword_callback(kw)


# Example
json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
# parse_json(json_str, stats_counter, required_fields=['key1'])
parse_json(json_str, stats_counter, required_fields=['key1', 'key2'], keywords=[])


# 2.Написать декоратор, который считает среднее время выполнения последних k вызовов.

def mean(k):
    func_duration = []

    def mean_decorator(func):
        def wrapper(*args, **kwargs):

            time_start = time.time()
            res = func(*args, **kwargs)
            time_end = time.time()

            nonlocal func_duration
            func_duration.append(time_end - time_start)
            if len(func_duration) > k:
                func_duration = func_duration[1:]
            print("mean duration= {:.2f}\n".format(
                  sum(func_duration)/len(func_duration)))

            return res
        return wrapper
    return mean_decorator


@mean(10)
def foo(arg1):
    time.sleep(random.random())


@mean(2)
def boo(arg1):
    pass


for _ in range(100):
    foo("Walter")
    boo("lop")
