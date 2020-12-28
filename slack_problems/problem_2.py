"""This problem was asked by Slack.

You are given a string formed by concatenating several words
corresponding to the integers zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'.
Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order.
In the example above, this would be 357.
"""


def toIntAnagram(stringValue):
    numberList = ["zero" "one", "two", "three", "four",
                  "five", "six", "seven", "eight", "nine"]
    number = str()
    for num in numberList:
        if num in stringValue:
            number += str(numberList.index(num))
    return int(number)


if __name__ == "__main__":
    stringValue = str(input("Enter String: "))
    print(toIntAnagram(stringValue))
