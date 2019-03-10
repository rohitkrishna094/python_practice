import re

# curly brackets can be used to specify the exact number of times you want to match a certain thing
# (Ha){3} means to match HaHaHa only
# (Ha){3,5} will match HaHaHa or HaHaHaHa or HaHaHaHaHa
# (Ha){3,} will match HaHaHa or more
# (Ha){,5} will match zero or more until 5 occurrences of Ha

hasRegex = re.compile(r'(Ha){3}')
mo1 = hasRegex.search('HaHaHa')
print(mo1.group())

mo2 = hasRegex.search('Ha')
print(mo2 == None)

# Greedy and Non-greedy matching
# (Ha){3,5} can match 3,4,5 Has, but mo gives the longest string match. In python default is greedy search
# To get non-greedy effect, we use ? symbol
# ? can be used two ways, one for flagging and optional group or for declaring a nongreedy match as shown below
print('----------------------Greedy')
greedyRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyRegex.search('HaHaHaHaHa')
print(mo1.group())


print('----------------------Non Greedy')
nongreedyRegex = re.compile(r'(Ha){3,5}?')
mo1 = nongreedyRegex.search('HaHaHaHaHa')
print(mo1.group())
