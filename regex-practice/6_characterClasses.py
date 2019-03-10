import re

# \d - matches digit
# \D - Any character that is not a numeric digit
# \w - any letter, numeric, underscore(essentially a word charcter)
# \W - negation of w
# \s - Any space, tab, newline
# \S - negation of \s

# matches text that has one or more digit, followed by a whitespace
# followed by one or more letter/digit/underscore chars.
xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese')
print(mo)

# make your own character classes
print('----------------')
# Try [aeiouAEIOU] will match all vowels
