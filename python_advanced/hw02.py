#Task 1. Определение чисел наиболее близких к нулю
#Написать функцию, которая принимает список чисел и возвращает список тех из них, 
# которые наиболее близки к нулю. 
# Из чисел [-5, 9, 6, -8] таковыми будут [-5], а из [-1, 2, -5, 1, -1] - [-1, 1, -1].


def get_zero_closest_nums(nums: list) -> list:
    zero_closest = []
    min_dist = float("+Inf")

    for n in nums:
        if abs(n) < min_dist:
            zero_closest = [n]
            min_dist = abs(n)
        elif abs(n) == min_dist:
            zero_closest.append(n)
    return zero_closest


print(f"\ntesting function {get_zero_closest_nums.__name__}\n", "-"*30)
assert get_zero_closest_nums([-5, 9, 6, -8]) == [-5]
assert get_zero_closest_nums([-1, 2, -5, 1, -1]) == [-1, 1, -1]
assert get_zero_closest_nums([]) == []
assert get_zero_closest_nums([1]) == [1]
assert get_zero_closest_nums([2, 2, 2]) == [2, 2, 2]
print("All tests passed: \n", "-"*30)


# 2. Слияние отсортированных списков без дубликатов
#Реализуйте функцию merge, которая принимает на вход две отсортированные по возрастанию 
# последовательности чисел и возвращает отсортированную последовательность, состоящую из 
# всех элементов, содержащихся в обоих исходных последовательностях без дубликатов.
#   Example:
#           lst = [1, 1, 2, 5, 7]
#           tp = (1, 1, 2, 3, 4, 7)
#           res = merge(lst, tp)
#           assert res == [1, 2, 7]

def merge(first_seq, second_seq):
    union_seq = set(first_seq) & set(second_seq)
    return sorted(union_seq)


print(f"\ntesting function {merge.__name__}\n", "-"*30)
assert merge([1, 1, 2, 5, 7], (1, 1, 2, 3, 4, 7)) == [1, 2, 7]
assert merge([], [3]) == []
assert merge([], []) == []
print("All tests passed: \n", "-"*30)