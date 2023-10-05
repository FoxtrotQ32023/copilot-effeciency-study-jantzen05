lines = None
with open('stringmultimatching.in') as f:
    lines = [ line.strip() for line in f ]

pattern_lines = 0
patterns_read = 0
pattern_list= []
for line in lines:
    # Start new pattern
    if line.isdigit():
        pattern_lines = int(line)
        patterns_read = 0
        pattern_list= []
    elif len(pattern_list) < pattern_lines:
        pattern_list.append(line)
    print(pattern_list)
