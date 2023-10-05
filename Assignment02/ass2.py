import re

LINES = None
RESULT_FILE = open("result_ass2.txt", "a")
with open('stringmultimatching.in') as f:
    LINES = [ line.strip() for line in f ]

PATTERN_LINES = 0
pattern_list= []
RESULT = None
for line in LINES:
    # Start new pattern
    if line.isdigit():
        PATTERN_LINES = int(line)
        pattern_list= []
    elif len(pattern_list) < PATTERN_LINES:
        pattern_list.append(line)
    else:
        for pattern in pattern_list:
            iter = re.finditer(pattern, line)
            for m in iter:
                RESULT_FILE.write(str(m.start()))
                RESULT_FILE.write(" ")
            RESULT_FILE.write("\n")
            
            
RESULT_FILE.close()
