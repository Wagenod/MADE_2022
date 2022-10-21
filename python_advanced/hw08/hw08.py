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
            tmp_cnt[letter] = tmp_cnt[letter] + 1 if letter in tmp_cnt else 1
            if tmp_cnt[letter] > pattern_cnt[letter]:
                shift = 1
                break
        else:
            anagrams.append(i)
    return anagrams


if __name__ == "__main__":
    txt = "abracadabra"
    search_str = "abra"
    print("{} indexes in {}: {}".format(search_str, txt, find_anagrams(txt, search_str)))
