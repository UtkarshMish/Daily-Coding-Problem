"""This problem was asked by MongoDB.

Given a list of elements, find the majority element,
which appears more than half the times (> floor(len(lst) / 2.0)).

You can assume that such element exists.
For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""
from math import floor


def findMajor(itemList: list) -> int or None:
    itemDict = dict()
    for item in itemList:
        if itemDict.get(item):
            itemDict[item] += 1
        else:
            itemDict[item] = 1
    for key, value in itemDict.items():
        if value >= floor(len(itemList)/2.0):
            return key

    return None


if __name__ == "__main__":
    listItems = [int(item) for item in input(
        "Enter elements with spaces: ").split(" ")]
    print(findMajor(listItems))
