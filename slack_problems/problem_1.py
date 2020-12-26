"""This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s. Starting from the top left corner,
how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[ [0, 0, 1],
  [0, 0, 1],
  [1, 0, 0]
  [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0.
"""


class ValueChecker():
    value = 0

    def calculate_ways(self, matrix, start=0, end=0, size={"m": 0, "n": 0}):
        if start == size["n"] and end == size["m"]:
            self.value += 1
            return
        elif start < 0 or end < 0 or start > size["n"] or end > size["m"]:
            return
        elif matrix[start][end] > 0:
            return
        else:
            self.calculate_ways(matrix, start=start, end=end+1, size=size)
            self.calculate_ways(matrix, start=start+1, end=end, size=size)


if __name__ == "__main__":
    n = int(input("Enter n(rows) value: "))
    m = int(input("Enter m(cols) value: "))
    matrix = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i].insert(j, int(input(f"Enter {i} & {j} value: ")))
    checker = ValueChecker()
    checker.calculate_ways(matrix, size={"m": m-1, "n": n-1})
    print(checker.value)
