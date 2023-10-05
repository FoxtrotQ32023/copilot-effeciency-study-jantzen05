"""This runs assignment 2"""
import os


def find_occurrences(string, substring):
    """Finds occurrences in string by the pattern

    Keyword arguments:
    strin -- the string to look in
    substring -- the pattern to look for

    """
    # Initialize count and start to 0
    start = 0
    positions = []

    # Search through the string till
    # we reach the end of it
    while start < len(string):

        # Check if a substring is present from
        # 'start' position till the end
        pos = string.find(substring, start)
        if pos != -1:
            # If a substring is present, move 'start' to
            # the next position from start of the substring
            positions.append(str(pos))
            start = pos + 1
        else:
            # If no further substring is present
            break
    # return the positions
    return positions


LINES = None
if os.path.isfile("result_ass2.txt"):
    os.remove("result_ass2.txt")
RESULT_FILE = open("result_ass2.txt", "a", encoding='utf-8')
with open('stringmultimatching.in', encoding='utf-8') as f:
    LINES = [ line.strip() for line in f ]

PATTERN_LINES = 0
pattern_list = []
for line in LINES:
    # Start new pattern
    if line.isdigit():
        PATTERN_LINES = int(line)
        pattern_list= []
    # The total length of all patterns in a test case is no more than 100.000.
    elif len(pattern_list) < PATTERN_LINES:
        if len(line) > 100000:
            raise TypeError("pattern to long")
        pattern_list.append(line)
    else:
        # The total length of line is no more than 200.000.
        if len(line) > 200000:
            raise TypeError("input line to long")
        for index, pattern in enumerate(pattern_list):
            OCC = find_occurrences(line, pattern)
            RESULT_FILE.write(" ".join(OCC) + "\n")
RESULT_FILE.close()
