from collections import Counter
from typing import List


def find_anagrams(text: str, pattern: str) -> List[int]:
    anagrams = []
    tmp_cnt = {}
    pattern_cnt = Counter(pattern)
    shift = 1

    for i in range(0, len(text) - len(pattern) + 1, shift):
        tmp_cnt = {}
        for k in range(len(pattern)):
            letter = text[i + k]
            if letter not in pattern_cnt:
                shift = k
                break
            else:
                if letter not in tmp_cnt:
                    tmp_cnt[letter] = 1
                else:
                    tmp_cnt[letter] += 1

                if tmp_cnt[letter] > pattern_cnt[letter]:
                    break
        else:
            anagrams.append(i)
    return anagrams


# def find_anagrams(text: str, pattern: str) -> List[int]:
#     anagrams = []
#     pattern_cnt = Counter(pattern)

#     for i in range(0, len(text) - len(pattern) + 1): # O(len(text))
#         if Counter(text[i: i + len(pattern)]) == pattern_cnt: # O(len(pattern))
#             anagrams.append(i)
#     return anagrams
    