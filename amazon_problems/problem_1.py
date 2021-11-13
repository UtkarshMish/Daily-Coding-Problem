"""This problem was asked by Amazon.
There exists a staircase with N steps, and you can climb up either 1 or 2 steps
at a time. Given N, write a function that returns the number of unique ways you can
 climb the staircase. The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:
•	1, 1, 1, 1
•	2, 1, 1
•	1, 2, 1
•	1, 1, 2
•	2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could
climb any number from a set of positive integers X? For example,
 if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time
"""
from typing import List


def check_value(arr_of_item: List[int], steps: int) -> -1 | 0 | 1:
    sum_of_arr = sum(arr_of_item)
    if sum_of_arr == steps:
        return 0
    elif sum_of_arr < steps:
        return -1
    else:
        return 1


def calc_ways(steps: List[int], total: int, **kwargs) -> List[List[int]]:
    choice: List[int] = kwargs.get("__choice") or []
    steps.sort()
    ways_list: List[List[int]] = list()
    for value in steps:
        choice.append(value)
        print(choice)
        isGreater = check_value(choice, total)
        if (value == total or isGreater == 0):
            if len(choice) != 0:
                ways_list.append(choice.copy())
            choice.pop()
            break
        elif isGreater == 1:
            choice.pop()
        else:
            item_list: List[List[int]] = list()
            item_list = calc_ways(steps, total, __choice=choice)
            if len(item_list) != 0:
                if not item_list == ways_list:
                    ways_list.extend(item_list)
            choice.pop()

    return ways_list


if __name__ == "__main__":
    steps = [1, 2, 3, 5,  7]
    N = 7
    print(calc_ways(steps, N))
