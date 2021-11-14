"""This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k
distinct characters is "bcb"."""

from typing import List


def check_if_exist(item: str, total: int) -> bool:
    distinct_char = list()
    for char in item:
        if not char in distinct_char:
            distinct_char.append(char)
        if len(distinct_char) > total:
            return False

    return True


def get_longest_distinct(num: int, str_value: str,) -> str:
    biggest_value = ""
    index = 0
    index_range = 1
    while index < (len(str_value)):
        for idx_2nd_pointer in range(index+index_range, len(str_value)):
            current_value = str_value[index: idx_2nd_pointer+1]
            isValueDistinct = check_if_exist(current_value, num)
            if isValueDistinct and len(biggest_value) < len(current_value):
                biggest_value = current_value
            else:
                break
            index_range += 1
        index += 1
    return biggest_value


if __name__ == "__main__":
    k: int = 2
    s: str = "fabeeqqbcbcbcabcbababa"
    print(get_longest_distinct(k, s))
